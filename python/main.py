import sys
import time

#input

field=input('高度人才分野?\na:高度学術研究分野\nb:高度専門・技術分野\nc:高度経営・管理分野\n')
education=input('education?\na:博士号（専門職に係る学位を除く。）取得者\nb:修士号（専門職に係る博士を含む。）取得者（注７）\nc:大学を卒業し又はこれと同等以上の教育を受けた者（博士号又は修士号取得者を除く。）\nd:none\n')
education_p1=input('複数の分野において，博士号，修士号又は専門職学位を複数有している者?\ny or n\n')
education_p2=input('経営管理に関する専門職学位（ＭＢＡ，ＭＯＴ）を有している?\ny or n\n')
career=int(input('職歴（実務経験）?\n'))
age=int(input('age?\n'))
incomes=int(input('imcome(万)?\n'))
research1=int(input('特許の発明何件?\n'))
research2=input('入国前に公的機関からグラントを受けた研究に従事した実績３件～?y/n\n')
research3=input('研究論文の実績については，我が国の国の機関において利用されている学術論文データベースに登録されている学術雑誌に掲載されている論文（申請人が責任著者であるものに限る。）?y/n\n')
research4=input('上記の項目以外で，上記項目におけるものと同等の研究実績があると申請人がアピールする場合（著名な賞の受賞歴等），関係行政機関の長の意見を聴いた上で法務大臣が個別にポイントの付与の適否を判断?y/n\n')
bonus4=input('イノベーションを促進するための支援措置（法務大臣が告示で定めるもの）を受けている機関における就労（注３）?\n')# Support measures to promote innovation.
bonus5=input('試験研究費等比率が３％超の中小企業における就労 y/n\n')# Small and medium-sized enterprises with a ratio of more than 3% for testing and research expenditure.
bonus6=input('職務に関連する外国の資格等 y/n\n')# Foreign qualifications relevant to the job, etc.
bonus10=input('成長分野における先端的事業に従事する者（法務大臣が認める事業に限る。）y/n\n')#Leading-edge projects in growth sectors
bonus11=input('法務大臣が告示で定める大学を卒業した者?y/n\n')# Universities specified by MOJ
bonus12=input('法務大臣が告示で定める研修を修了した者?y/n\n')# Training prescribed by MOJ
bonus7= input('本邦の高等教育機関において学位を取得y/n?\n')# Degree from a Japanese higher education institution.
bonus8_9=input('a.N1 or b.N2 or c.none?\n')# JLPT
bonus2=input('a.代表取締役，代表執行役 b.取締役，執行役 c.none\n')# Positions in the company
bonus3=int(input('職務に関連する日本の国家資格の保有（１つ５点）'))#Japanese national qualifications relevant to the job.
bonus13=input('経営する事業に１億円以上の投資を行っている者?y/n\n')# Investing more than 100 million in the business you run
bonus14=input('投資運用業等に係る業務に従事?y/n\n')# Engaged in operations related to investment management business

#functions

def score_education(field, education):
    if field=='a' or 'b' and education=='a':
        return 30
    elif field=='a' or 'b' or 'c' and education=='b':
        return 20
    elif field=='a' or 'b' or 'c' and education=='c':
        return 10
    elif field=='c' and education=='a':
        return 20
    else:
         return 0
def score_education_p1(field, education_p1):
    if field=='b' or'c':
        if  education_p1=='y':
            return 5
        elif  education_p1=='n':
            return 0
    else:
         return 0
def score_education_p2(field, education_p2):
    if field=='b' or'c':
        if  education_p2=='y':
            return 5
        elif  education_p2=='n':
            return 0
    else:
         return 0
def score_career(field, career):
    if field=='c':
        if  career<3:
            return 0
        elif  3<=career<5:
            return 10
        elif  5<=career<7:
            return 15
        elif  7<=career<10:
            return 20
        elif  10<=career:
            return 25
    elif field=='a' or 'b':
        if  career<3:
            return 0
        elif  3<=career<5:
            return 5
        elif  5<=career<7:
            return 10
        elif  7<=career<10:
            return 15
    elif field =='b' and career>=10:
            return 20
def score_age(age,field):
    if field=='a' or 'b':
        if  age < 29:
            return 15
        elif  age <34:
            return 10
        elif  age <39:
            return 5
        elif  age >39:
            return 0
    elif field=='c':
        pass
def score_income(age,incomes,field):
    if field=='a' or 'b':
        if  400<=incomes<500 and age<29:
            return 10
        elif  500<=incomes<600 and age<34:
            return 15
        elif  600<=incomes<700 and age<39:
            return 20
        elif  700<=incomes<800 and age<39:
            return 25
        elif  800<=incomes<900:
            return 30
        elif  900<=incomes<1000:
            return 35
        elif  incomes>=1000:
            return 40
        elif  300<=incomes<400:
            return 0
    elif field=='c':
        if  300<=incomes<1000:
            return 0
        elif  1000<=incomes<1500:
            return 10
        elif  1500<=incomes<2000:
            return 20
        elif  2000<=incomes<2500:
            return 30
        elif  2500<=incomes<3000:
            return 40
        elif  incomes>=3000:
            return 50
    elif field=='b' or 'c' and incomes<300:
            print('高度専門・技術分野及び高度経営・管理分野においては，年収３００万円以上であることが必要')
            time.sleep(10)
            sys.exit(0)
if field=='a' or 'b':
    if research1==1:
            score_research1=20
    elif research1>1:
            score_research1=25
    else:
            score_research1=0
    if research2=='y':
            score_research2=15
    else:
            score_research2=0
    if research3=='y':
            score_research3=15
    else:
            score_research3=0
    if research4=='y':
            score_research4=15
    else:
            score_research4=0
    score_research=score_research1+score_research2+score_research3+score_research4
else:
    score_research = 0
score_bonus=0
if bonus4=='y':
        score_bonus=score_bonus+10
else:
        score_bonus=score_bonus+0
if bonus5=='y':
        score_bonus=score_bonus+5
else:
        score_bonus=score_bonus+0
if bonus6=='y':
        score_bonus=score_bonus+5
else:
        score_bonus=score_bonus+0
if bonus10=='y':
        score_bonus=score_bonus+10
else:
        score_bonus=score_bonus+0
if bonus11=='y':
        score_bonus=score_bonus+10
else:
        score_bonus=score_bonus+0
if bonus12=='y':
        score_bonus=score_bonus+10
else:
        score_bonus=score_bonus+0

def score_bonus_jlpt(bonus7, bonus8_9):
      if bonus8_9=='a' and bonus7=='y':
            return 25
      elif bonus8_9=='a' and bonus7=='n':
            return 15
      else:
            return 10
score_bonus2=0
score_bonus3=0
score_bonus4=0
score_bonus13=0
score_bonus14=0
if field=='b':
    if bonus3>=2:
        score_bonus3+=10
    elif bonus3==1:
        score_bonus3+=5
    else:
        score_bonus3+=0
    if bonus14=='y':
        score_bonus4+=10
    else:
        score_bonus4+=0
elif field=='c':
    if bonus2=='a':
        score_bonus2+=10
    elif bonus2=='b':
        score_bonus2+=5
    else:
        score_bonus2+=0
    if bonus13=='y':
        score_bonus13+=5
    else:
        score_bonus13+=0
    if bonus14=='y':
        score_bonus14+=10
    else:
        score_bonus14+=0
    
score_bonus_other = score_bonus2+score_bonus3+score_bonus4+score_bonus13+score_bonus14

score_sum = {
        'score_education':score_education(field, education),
        'score_education_p1':score_education_p1(field, education_p1),
        'score_education_p2':score_education_p2(field, education_p2),
        'score_career':score_career(field, career),
        'score_incomes':score_income(age,incomes,field),
        'score_age':score_age(age,field),
        'score_bonus':score_bonus,
        'score_research':score_research,
        'score_bonus5':score_bonus_jlpt(bonus7, bonus8_9),
        'score_bonus_other':score_bonus_other
}
score_result = sum(score_sum.values())
print(score_result)
if score_result>70:
        print('合格')
else:
        print('')
         
    
