#프로젝트 코드 중 일부
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #키입력시 사용용
import time # 대기시간 필요할거같아서 넣음
import pymysql
import pandas as pd
import csv

# browser = webdriver.Chrome("./chromedriver.exe")
browser = webdriver.Chrome()
browser.implicitly_wait(10)
################### 잡코리아################################

browser.get("https://www.jobkorea.co.kr/")

jobkorea = browser.find_element_by_class_name("btnMyOpen")
jobkorea.click()
# 여기로 로그인 하는게 편함 - 공식홈페이지에서 개인회원 로그인창 누르면 팝업형식이라 모르는 형식

jobkorea = browser.find_element_by_id("M_ID")  # 꼭 자바스크립트 클래스가 아니라 , class 옆 name 도 가능
jobkorea.send_keys("MY_ID")  # 수정
time.sleep(1)

jobkorea = browser.find_element_by_id("M_PWD")  # 꼭 자바스크립트 클래스가 아니라 , class 옆 name 도 가능
jobkorea.send_keys("MY_PWD")  # 수정
time.sleep(1)

# 로그인 버튼 클릭
jobkorea = browser.find_element_by_xpath("//*[@id='form']/fieldset/div[3]/button")
jobkorea.click()
# xpath로 하니 쉽게 로그인

Company_name = []  # 기업 리스트 선언

browser.get(
    "https://www.jobkorea.co.kr/Top100/?Main_Career_Type=1&Search_Type=1&BizJobtype_Bctgr_Code=10016&BizJobtype_Bctgr_Name=IT%C2%B7%EC%9D%B8%ED%84%B0%EB%84%B7&BizJobtype_Code=0&BizJobtype_Name=IT%C2%B7%EC%9D%B8%ED%84%B0%EB%84%B7+%EC%A0%84%EC%B2%B4&Major_Big_Code=0&Major_Big_Name=%EC%A0%84%EC%B2%B4&Major_Code=0&Major_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Code=9&Edu_Level_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Name=%EC%A0%84%EC%B2%B4&MidScroll=0")
# 링크로 이동

jobkorea1 = browser.find_element_by_xpath(
    "/html/body/div[5]/div[1]/div/form/div[2]/div/div[2]/div[1]/ol/li[1]/div[1]/span")
jobkorea1

jobkorea2 = browser.find_element_by_xpath("/html/body/div[5]/div[1]/div/form/div[2]/div/div[2]/div[1]/ol/li[2]/div[1]")
jobkorea2

jobkorea3 = browser.find_element_by_xpath(
    "/html/body/div[5]/div[1]/div/form/div[2]/div/div[2]/div[1]/ol/li[2]/div[2]/div[1]/a/b")
jobkorea3

jobkorea1.text

jobkorea2.text

jobkorea3.text

Company_name.append(jobkorea3.text)

Company_name

# 여기까지 기록 보관용

Company_name = []  # 기업 리스트 선언

for i in range(1, 101):
    jobkorea_0 = browser.find_element_by_xpath(
        "/html/body/div[5]/div[1]/div/form/div[2]/div/div[2]/div[1]/ol/li[{0}]/div[2]/div[1]/a/b".format(i))
    Company_name.append(jobkorea_0.text)
# 1부터 받아야함 li[1]이 시작
Company_name

######################### 잡플래닛##########################################

browser.get("https://www.jobplanet.co.kr/welcome/index")

# 로그인 해야 기업리뷰 볼 수 있다
jobplanet = browser.find_element_by_class_name("btn_txt")
jobplanet.click()

browser.implicitly_wait(10)
browser.implicitly_wait(10)

jobplanet = browser.find_element_by_id("user_email")  # 꼭 자바스크립트 클래스가 아니라 , class 옆 name 도 가능
jobplanet.send_keys("MY_ID")  # 수정
time.sleep(1)

jobplanet = browser.find_element_by_id("user_password")  # 꼭 자바스크립트 클래스가 아니라 , class 옆 name 도 가능
jobplanet.send_keys("MY_PWD")  # 수정
time.sleep(1)

jobplanet = browser.find_element_by_class_name("btn_sign_up")
jobplanet.click()
time.sleep(1)
# 리뷰, 연봉(대졸기준), 면접, 복지

###############리스트 선언###############
jobplanet_rate_csv = []  # 기업리뷰, 전체 통계
jobplanet_Welfare_Salary_csv = []  # 기업리뷰 세분화 - 복지 및 급여
jobplanet_Work_Life_csv = []  # 기업리뷰 세분화 - 업무와 삶의 균형
jobplanet_Work_Culture_csv = []  # 기업리뷰 세분화 - 사내문화
jobplanet_possible_csv = []  # 기업리뷰 세분화 - 승진 기회 및 가능성
jobplanet_Management_csv = []  # 기업리뷰 세분화 - 경영진
joplanet_Salary_1_csv = []  # 사원 대졸인지 확인용  - 왠지 sql에 넣을때 사원-대졸인지 확인용으로 사용될듯
joplanet_Salary_money_csv = []  # 사원-대졸 연봉  - 만원기준
joplanet_Interview_csv = []  # 기업 면접 난이도 - 0~5 기준이라고 출력하기
jobplanet_Welfare_csv = []  # 기업 복지 - 전체 복지 통계

##########################팝업창 제거용############################

jobplanet = browser.find_element_by_id("search_bar_search_query")

jobplanet.send_keys(Company_name[0])

jobplanet.send_keys(Keys.ENTER)

joplanet = browser.find_element_by_xpath(
    "/html/body/div[1]/div[3]/div/div[1]/div[1]/div/div[2]/div[1]/div[1]/span[1]/a/img")
joplanet.click()
time.sleep(5)
# 팝업청 끄기용으로 시간늘리

# 기업창 팝업이 뜸 항상 눌러야 하나  - 이게 한번만 뜨는 상황임 그래서 앞으로 빼내어서 실행 1번만 되게함
jobplanet = browser.find_element_by_class_name("btn_close_x_ty1 ")
jobplanet.click()

####################################################################
############반복문은 15개로 테스트용 ############################## 여기밑에 for문을 15개에서 101로 바꾸면 됩니다

for i in range(0, 101):
    print("===============", i)
    #########################
    # 참고로 반복문 넣어야함 #
    try:
        #########################
        # 참고로 반복문 넣어야함 #
        print(Company_name[i])

        jobplanet = browser.find_element_by_id("search_bar_search_query")
        jobplanet.send_keys(Company_name[i])
        jobplanet.send_keys(Keys.ENTER)

        joplanet = browser.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[1]/div/div[2]/div[1]/div[1]/span[1]/a/img")
        joplanet.click()

        # 리뷰선택하기 - 다른 회사는 뉴스룸이 먼저 뜨는 경우도 있음
        jobplanet_rate = browser.find_element_by_class_name("viewReviews")
        jobplanet_rate.click()
        time.sleep(2)

        # 기업 리뷰, 전체 통계
        jobplanet_rate = browser.find_element_by_class_name("rate_point")
        jobplanet_rate.text
        jobplanet_rate_csv.append(jobplanet_rate.text)

        time.sleep(2)

        try:
            # 기업리뷰 세분화 - 복지 및 급여
            jobplanet_Welfare_Salary = browser.find_element_by_xpath(
                "/html/body/div[1]/div[4]/div/div[1]/div[1]/div/div/div/div[2]/div[2]/div[1]/div/div[2]/span[2]")
            jobplanet_Welfare_Salary.text
            jobplanet_Welfare_Salary_csv.append(jobplanet_Welfare_Salary.text)
            print("복지 및 급여 0~5기준=", jobplanet_Welfare_Salary.text)

            # 기업리뷰 세분화 - 업무와 삶의 균형
            jobplanet_Work_Life = browser.find_element_by_xpath(
                "/html/body/div[1]/div[4]/div/div[1]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div[2]/span[2]")
            jobplanet_Work_Life.text
            jobplanet_Work_Life_csv.append(jobplanet_Work_Life.text)
            print("업무와 삶의 균형  0~5기준=", jobplanet_Work_Life.text)

            # 기업리뷰 세분화 - 사내문화
            jobplanet_Work_Culture = browser.find_element_by_xpath(
                "/html/body/div[1]/div[4]/div/div[1]/div[1]/div/div/div/div[2]/div[2]/div[3]/div/div[2]/span[2]")
            jobplanet_Work_Culture.text
            jobplanet_Work_Culture_csv.append(jobplanet_Work_Culture.text)
            print("사내문화 0~5기준=", jobplanet_Work_Culture.text)

            # 기업리뷰 세분화 - 승진 기회 및 가능성
            jobplanet_possible = browser.find_element_by_xpath(
                "/html/body/div[1]/div[4]/div/div[1]/div[1]/div/div/div/div[2]/div[2]/div[4]/div/div[2]/span[2]")
            jobplanet_possible.text
            jobplanet_possible_csv.append(jobplanet_possible.text)
            print("승진 기회 및 가능성 0~5기준=", jobplanet_possible.text)

            # 기업리뷰 세분화 - 경영진
            jobplanet_Management = browser.find_element_by_xpath(
                "/html/body/div[1]/div[4]/div/div[1]/div[1]/div/div/div/div[2]/div[2]/div[5]/div/div[2]/span[2]")
            jobplanet_Management.text
            jobplanet_Management_csv.append(jobplanet_Management.text)
            print("경영진 0~5기준=", jobplanet_Management.text)

            # 기업연봉 - 초대졸 기준으로 확인
            joplanet_Salary = browser.find_element_by_class_name("viewSalaries")
            joplanet_Salary.click()
            time.sleep(2)

            # 여기서 문제네 첫번째 칸이 초대졸이 맞는가?
            # 다행이도 첫번째 칸이 사원-대졸인듯 5개 정도 확인
            # 사원 대졸인지 확인용  - 왠지 sql에 넣을때 사원-대졸인지 확인용으로 사용될듯
            # 연봉이 없는 경우가 있다 그래서 계속 실행되게 해야함
            try:
                joplanet_Salary_1 = browser.find_element_by_xpath(
                    "/html/body/div[1]/div[4]/div/div[1]/div[4]/article/div[1]/div/div[2]/ul[2]/li[1]/a")
                joplanet_Salary_1.text
                joplanet_Salary_1_csv.append(joplanet_Salary_1.text)

                # 사원-대졸 연봉  - 만원기준
                joplanet_Salary_money = browser.find_element_by_xpath(
                    "/html/body/div[1]/div[4]/div/div[1]/div[4]/article/div[1]/div/div[2]/ul[2]/li[2]/strong/strong")
                joplanet_Salary_money.text
                joplanet_Salary_money_csv.append(joplanet_Salary_money.text)

                money = joplanet_Salary_money.text
                print("사원-대졸 연봉 " + str(money) + "만원")

            except:  # 연봉이 없을 경우
                print("연봉이 없습니다")
                joplanet_Salary_1_csv.append("--")
                joplanet_Salary_money_csv.append("0")

                # 기업 면접
                joplanet_Interview = browser.find_element_by_class_name("viewInterviews")
                joplanet_Interview.click()
                time.sleep(2)

                # 기업 면접 난이도 - 0~5 기준이라고 출력하기
                joplanet_Interview = browser.find_element_by_class_name("vib_num")
                joplanet_Interview.text
                joplanet_Interview_csv.append(joplanet_Interview.text)
                print("기업 면접 난이도 0~5기준=", joplanet_Interview.text)

                # 기업 복지 - 전체 복지 통계
                jobplanet_Welfare = browser.find_element_by_class_name("viewWelfare")
                jobplanet_Welfare.click()
                time.sleep(3)

                jobplanet_Welfare = browser.find_element_by_class_name("rate_point")
                jobplanet_Welfare.text
                jobplanet_Welfare_csv.append(jobplanet_Welfare.text)
                print("기업 복지 0~5기준=", jobplanet_Welfare.text)
                print("기업정보 완료")  # print문 잘 사용해봐
                continue

            # 기업 면접
            joplanet_Interview = browser.find_element_by_class_name("viewInterviews")
            joplanet_Interview.click()
            time.sleep(2)

            # 기업 면접 난이도 - 0~5 기준이라고 출력하기
            joplanet_Interview = browser.find_element_by_class_name("vib_num")
            joplanet_Interview.text
            joplanet_Interview_csv.append(joplanet_Interview.text)
            print("기업 면접 난이도 0~5기준=", joplanet_Interview.text)

            # 기업 복지 - 전체 복지 통계
            jobplanet_Welfare = browser.find_element_by_class_name("viewWelfare")
            jobplanet_Welfare.click()
            time.sleep(3)

            jobplanet_Welfare = browser.find_element_by_class_name("rate_point")
            jobplanet_Welfare.text
            jobplanet_Welfare_csv.append(jobplanet_Welfare.text)
            print("기업 복지 0~5기준=", jobplanet_Welfare.text)
            print("기업정보 완료")  # print문 잘 사용해봐

        except:  #################골든하인드 같은 - 리뷰가 연도마다 다를경우 ### 페이지 모습이 달라짐
            # 기업리뷰 세분화 - 복지 및 급여
            jobplanet_Welfare_Salary = browser.find_element_by_xpath(
                "/html/body/div[1]/div[4]/div/div[1]/div[1]/div[2]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span[2]")
            jobplanet_Welfare_Salary.text
            jobplanet_Welfare_Salary_csv.append(jobplanet_Welfare_Salary.text)
            print("복지 및 급여 0~5기준=", jobplanet_Welfare_Salary.text)

            # 기업리뷰 세분화 - 업무와 삶의 균형
            jobplanet_Work_Life = browser.find_element_by_xpath(
                "/html/body/div[1]/div[4]/div/div[1]/div[1]/div[2]/div[1]/div/div[3]/div[2]/div[2]/div/div[2]/span[2]")
            jobplanet_Work_Life.text
            jobplanet_Work_Life_csv.append(jobplanet_Work_Life.text)
            print("업무와 삶의 균형  0~5기준=", jobplanet_Work_Life.text)

            # 기업리뷰 세분화 - 사내문화
            jobplanet_Work_Culture = browser.find_element_by_xpath(
                "/html/body/div[1]/div[4]/div/div[1]/div[1]/div[2]/div[1]/div/div[3]/div[2]/div[3]/div/div[2]/span[2]")
            jobplanet_Work_Culture.text
            jobplanet_Work_Culture_csv.append(jobplanet_Work_Culture.text)
            print("사내문화 0~5기준=", jobplanet_Work_Culture.text)

            # 기업리뷰 세분화 - 승진 기회 및 가능성
            jobplanet_possible = browser.find_element_by_xpath(
                "/html/body/div[1]/div[4]/div/div[1]/div[1]/div[2]/div[1]/div/div[3]/div[2]/div[4]/div/div[2]/span[2]")
            jobplanet_possible.text
            jobplanet_possible_csv.append(jobplanet_possible.text)
            print("승진 기회 및 가능성 0~5기준=", jobplanet_possible.text)

            # 기업리뷰 세분화 - 경영진
            jobplanet_Management = browser.find_element_by_xpath(
                "/html/body/div[1]/div[4]/div/div[1]/div[1]/div[2]/div[1]/div/div[3]/div[2]/div[5]/div/div[2]/span[2]")
            jobplanet_Management.text
            jobplanet_Management_csv.append(jobplanet_Management.text)
            print("경영진 0~5기준=", jobplanet_Management.text)

            # 기업연봉 - 초대졸 기준으로 확인
            joplanet_Salary = browser.find_element_by_class_name("viewSalaries")
            joplanet_Salary.click()
            time.sleep(2)

            # 여기서 문제네 첫번째 칸이 초대졸이 맞는가?
            # 다행이도 첫번째 칸이 사원-대졸인듯 5개 정도 확인
            # 사원 대졸인지 확인용  - 왠지 sql에 넣을때 사원-대졸인지 확인용으로 사용될듯
            # 연봉이 없는 경우가 있다 그래서 계속 실행되게 해야함
            try:
                joplanet_Salary_1 = browser.find_element_by_xpath(
                    "/html/body/div[1]/div[4]/div/div[1]/div[4]/article/div[1]/div/div[2]/ul[2]/li[1]/a")
                joplanet_Salary_1.text
                joplanet_Salary_1_csv.append(joplanet_Salary_1.text)

                # 사원-대졸 연봉  - 만원기준
                joplanet_Salary_money = browser.find_element_by_xpath(
                    "/html/body/div[1]/div[4]/div/div[1]/div[4]/article/div[1]/div/div[2]/ul[2]/li[2]/strong/strong")
                joplanet_Salary_money.text
                joplanet_Salary_money_csv.append(joplanet_Salary_money.text)

                money = joplanet_Salary_money.text
                print("사원-대졸 연봉 " + str(money) + "만원")

            except:  # 연봉이 없을 경우
                print("연봉이 없습니다")
                joplanet_Salary_1_csv.append("--")
                joplanet_Salary_money_csv.append("0")

                # 기업 면접
                joplanet_Interview = browser.find_element_by_class_name("viewInterviews")
                joplanet_Interview.click()
                time.sleep(2)

                # 기업 면접 난이도 - 0~5 기준이라고 출력하기
                joplanet_Interview = browser.find_element_by_class_name("vib_num")
                joplanet_Interview.text
                joplanet_Interview_csv.append(joplanet_Interview.text)
                print("기업 면접 난이도 0~5기준=", joplanet_Interview.text)

                # 기업 복지 - 전체 복지 통계
                jobplanet_Welfare = browser.find_element_by_class_name("viewWelfare")
                jobplanet_Welfare.click()
                time.sleep(3)

                jobplanet_Welfare = browser.find_element_by_class_name("rate_point")
                jobplanet_Welfare.text
                jobplanet_Welfare_csv.append(jobplanet_Welfare.text)
                print("기업 복지 0~5기준=", jobplanet_Welfare.text)
                print("기업정보 완료")  # print문 잘 사용해봐
                continue

            # 기업 면접
            joplanet_Interview = browser.find_element_by_class_name("viewInterviews")
            joplanet_Interview.click()
            time.sleep(2)

            # 기업 면접 난이도 - 0~5 기준이라고 출력하기
            joplanet_Interview = browser.find_element_by_class_name("vib_num")
            joplanet_Interview.text
            joplanet_Interview_csv.append(joplanet_Interview.text)
            print("기업 면접 난이도 0~5기준=", joplanet_Interview.text)

            # 기업 복지 - 전체 복지 통계
            jobplanet_Welfare = browser.find_element_by_class_name("viewWelfare")
            jobplanet_Welfare.click()
            time.sleep(3)

            jobplanet_Welfare = browser.find_element_by_class_name("rate_point")
            jobplanet_Welfare.text
            jobplanet_Welfare_csv.append(jobplanet_Welfare.text)
            print("기업 복지 0~5기준=", jobplanet_Welfare.text)
            print("기업정보 완료")  # print문 잘 사용해봐


    except:
        print("기업이 없습니다")
        jobplanet_rate_csv.append("0")
        jobplanet_Welfare_Salary_csv.append("0")
        jobplanet_Work_Life_csv.append("0")
        jobplanet_Work_Culture_csv.append("0")
        jobplanet_possible_csv.append("0")
        jobplanet_Management_csv.append("0")
        joplanet_Salary_1_csv.append("0")
        joplanet_Salary_money_csv.append("0")
        joplanet_Interview_csv.append("0")
        jobplanet_Welfare_csv.append("0")  # 없는 항목을 0으로 추가한다
        browser_clear = browser.find_element_by_class_name("input_search").clear()  # 없는기업이 검색창에 남아서 지워준다
        continue

print(jobplanet_rate_csv,
      jobplanet_Welfare_Salary_csv,
      jobplanet_Work_Life_csv,
      jobplanet_Work_Culture_csv,
      jobplanet_possible_csv,
      jobplanet_Management_csv,
      joplanet_Salary_1_csv,
      joplanet_Salary_money_csv,
      joplanet_Interview_csv,
      jobplanet_Welfare_csv)


with open('company_test.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(Company_name)
    writer.writerow(jobplanet_rate_csv)
    writer.writerow(jobplanet_Welfare_Salary_csv)
    writer.writerow(jobplanet_Work_Life_csv)
    writer.writerow(jobplanet_Work_Culture_csv)
    writer.writerow(jobplanet_possible_csv)
    writer.writerow(jobplanet_Management_csv)
    writer.writerow(joplanet_Salary_1_csv)
    writer.writerow(joplanet_Salary_money_csv)
    writer.writerow(joplanet_Interview_csv)
    writer.writerow(jobplanet_Welfare_csv)
# 만약 기업이 없습니다 뜨면 숫자 확인하기
# 마지막에 csv가 000으로 맞춰떠야함