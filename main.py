# 웹 요청(urllib), JSON 파싱(json), GUI 구성(tkinter 및 font)을 위한 필수 모듈
import urllib.request, json, tkinter, tkinter.font
 
# OpenWeatherMap 사이트에서 발급받은 개인 API 키를 저장하는 변수.
API_KEY = "Enter your API key here"
 
# 날씨 데이터를 요청하고 GUI 화면을 업데이트하는 함수.
def tick1Min():
    # 서울(Seoul)의 현재 날씨를 섭씨(metric) 단위로 요청하기 위한 API 주소(URL)를 문자열 포매팅(f-string)으로 생성.
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Seoul&appid={API_KEY}&units=metric"
    # 생성한 URL로 웹 서버에 접속하여 데이터를 요청하고, 응답 결과 객체를 'r'이라는 이름으로 열기.
    with urllib.request.urlopen(url) as r:
        data = json.loads(r.read())               # 서버로부터 읽어온 텍스트(JSON 형태)를 파이썬에서 다루기 쉽도록 딕셔너리(Dictionary) 형태로 변환하여 'data'에 저장
    temp = data["main"]["temp"]                   # JSON 구조를 파싱하여 'main' 항목 안에 있는 'temp'(온도) 값을 추출.
    humi = data["main"]["humidity"]               # 동일하게 'main' 항목 안에 있는 'humidity'(습도) 값을 추출.
    
    label.config(text=f"{temp:.1f}C   {humi}%")   # 추출한 온도(소수점 1자리까지 표시)와 습도 값으로 GUI 레이블 위젯의 텍스트 내용을 갱신.
    window.after(60000, tick1Min)                 # 60,000ms(1분) 후에 이 함수(tick1Min)를 다시 실행하도록 예약하여 지속적으로 데이터 갱신.
 
window = tkinter.Tk()                             # tkinter를 사용하여 프로그램의 메인 윈도우(GUI 창) 객체를 생성
window.title("TEMP HUMI DISPLAY")                 # 창 상단 제목 표시줄의 이름을 설정.
window.geometry("400x100")                        # 창의 크기를 가로 400픽셀, 세로 100픽셀로 설정.
window.resizable(False, False)                    # 사용자가 마우스로 창의 가로, 세로 크기를 조절할 수 없도록 크기를 고정.
font = tkinter.font.Font(size=30)                 # 화면에 표시될 글자의 크기를 30으로 설정한 폰트 객체를 생성.
label = tkinter.Label(window, text="", font=font) # 생성한 창(window) 내부에 폰트 크기가 30인 빈 텍스트 레이블(Label) 위젯을 생성.
label.pack()                                      # 레이블 위젯을 창 내부 중앙에 알맞게 자동 배치.
tick1Min()                                        # 프로그램이 켜지자마자 날씨 정보를 즉시 불러오기 위해 함수를 최초 1회 호출.
window.mainloop()                                 # GUI 창이 즉시 꺼지지 않고 사용자 동작이나 예약된 작업(after 메서드 등)을 계속 처리하도록 무한 이벤트 루프를 실행.
