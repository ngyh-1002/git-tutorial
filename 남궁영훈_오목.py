# 작동방식 터틀인터페이스를 이용해서 오목게임 하기
'''
1. colormode메소드와 penup, pendown을 이용해서 바둑판을 그린다.
2. 한칸 사이즈를 40으로 설정해 좌표값을 지정한다.
3. 좌표값과 turtle모듈의 onclick메소드로 바둑돌을 인터페이스에서 클릭으로 놓게설정
4. 오목방향을 확인하기위해 가로세로 대각선을확인하기위한 단위벡터 리스트를 작성한뒤 반복문으로 확인
5. 오목이 확인되면 승자 결정
'''
import turtle

# --- 게임 설정 ---
BOARD_SIZE = 19  # 바둑판 줄 수 (19x19)
CELL_SIZE = 40   # 한 칸의 크기 (픽셀)
BOARD_OFFSET = (BOARD_SIZE // 2) * CELL_SIZE # 보드 중심을 위한 오프셋

# --- 터틀 스크린 설정 ---
screen = turtle.Screen()
screen.setup(width=900, height=900) # 윈도우 크기 설정
screen.colormode(255)
screen.bgcolor(255, 166, 72) # 오목판 색상 (어두운 주황색 계열)
screen.tracer(0) # 화면 업데이트를 수동으로 제어하여 그리기 속도 향상

# --- 메시지 터틀 설정 ---
message_turtle = turtle.Turtle()
message_turtle.hideturtle()
message_turtle.penup()
message_turtle.goto(0, screen.window_height() / 2 - 50) # 화면 상단에 위치
message_turtle.color("red")
message_turtle.write("흑돌부터 시작!", align="center", font=("Arial", 24, "bold"))

# --- 바둑판 그리기 함수 ---
def draw_board():
    board_turtle = turtle.Turtle()
    board_turtle.speed(0)
    board_turtle.pencolor("black")
    board_turtle.pensize(2)
    board_turtle.hideturtle()

    start_x = -BOARD_OFFSET
    start_y = -BOARD_OFFSET

    # 가로선 그리기
    for i in range(BOARD_SIZE):
        board_turtle.penup()
        board_turtle.goto(start_x, start_y + i * CELL_SIZE)
        board_turtle.pendown()
        board_turtle.forward(CELL_SIZE * (BOARD_SIZE - 1))

    # 세로선 그리기
    board_turtle.left(90) # 90도 회전하여 세로선 그릴 준비
    for i in range(BOARD_SIZE):
        board_turtle.penup()
        board_turtle.goto(start_x + i * CELL_SIZE, start_y)
        board_turtle.pendown()
        board_turtle.forward(CELL_SIZE * (BOARD_SIZE - 1))
    screen.update() # 화면 업데이트

# --- 돌 관리 ---
board = [['.' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)] # 게임 보드 상태 저장
player_turn = 0 # 0: 흑돌, 1: 백돌
stones = [] # 놓여진 돌 터틀 객체 저장

# --- 돌 놓기 함수 ---
def place_stone(x, y):
    global player_turn

    # 클릭된 좌표를 가장 가까운 교차점으로 변환
    grid_x = round((x + BOARD_OFFSET) / CELL_SIZE)
    grid_y = round((y + BOARD_OFFSET) / CELL_SIZE)

    # 유효한 범위인지 확인
    if not (0 <= grid_x < BOARD_SIZE and 0 <= grid_y < BOARD_SIZE):
        return

    # 이미 돌이 놓여있는지 확인
    if board[grid_y][grid_x] != '.':
        return

    stone_turtle = turtle.Turtle()
    stone_turtle.speed(0)
    stone_turtle.shape("circle")
    stone_turtle.shapesize(CELL_SIZE / 20) # 돌 크기 조절
    stone_turtle.penup()

    # 돌 색상 설정 및 보드 상태 업데이트
    if player_turn == 0:
        stone_turtle.color("black")
        board[grid_y][grid_x] = 'B' # Black
    else:
        stone_turtle.color("white")
        board[grid_y][grid_x] = 'W' # White

    # 돌을 정확한 교차점 위치로 이동
    stone_x = grid_x * CELL_SIZE - BOARD_OFFSET
    stone_y = grid_y * CELL_SIZE - BOARD_OFFSET
    stone_turtle.goto(stone_x, stone_y)
    stones.append(stone_turtle) # 놓여진 돌 저장

    screen.update() # 화면 업데이트

    # 승리 판정
    if check_win(grid_x, grid_y, board[grid_y][grid_x]):
        winner = "흑돌" if player_turn == 0 else "백돌"
        message_turtle.clear()
        message_turtle.write(f"{winner} 승리!", align="center", font=("Arial", 24, "bold"))
        # 게임 종료 또는 다시 시작 기능 추가 가능
        screen.onclick(None) # 더 이상 클릭 못하게 함
        return

    # 턴 변경
    player_turn = 1 - player_turn

# --- 승리 판정 함수 ---
def check_win(x, y, player):
    # 가로, 세로, 두 가지 대각선 방향 확인
    directions = [
        (1, 0),  # 가로
        (0, 1),  # 세로
        (1, 1),  # 대각선 (우상향)
        (1, -1)  # 대각선 (우하향)
    ]

    for dx, dy in directions:
        count = 1
        # 정방향 확인
        for i in range(1, 5):
            nx, ny = x + i * dx, y + i * dy
            if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and board[ny][nx] == player:
                count += 1
            else:
                break
        # 역방향 확인
        for i in range(1, 5):
            nx, ny = x - i * dx, y - i * dy
            if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and board[ny][nx] == player:
                count += 1
            else:
                break
        if count >= 5:
            return True
    return False

# --- 게임 시작 ---
draw_board() # 바둑판 그리기
screen.onclick(place_stone) # 마우스 클릭 이벤트 핸들러 등록

turtle.done() # 윈도우를 닫히지 않게 유지