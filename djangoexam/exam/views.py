from datetime import datetime
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from . import models
from django.db.models import Q
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta


# 学生登录
def studentLogin(request):
    if request.method == 'POST':
        # 获取表单信息
        sid = request.POST.get('sid')
        password = request.POST.get('password')
        print("sid", sid, "password", password)
        # 通过学号获取该学生实体
        student = models.Student.objects.filter(sid=sid).values('pwd')

        if student.exists():
            student = models.Student.objects.get(sid=sid)
            if password == student.pwd:  # 登录成功
                request.session['username'] = sid
                request.session['is_login'] = True
                # 查询考试信息
                paper = models.TestPaper.objects.filter(major=student.major)
                # 查询成绩信息
                grade = models.Record.objects.filter(sid=student.sid)

                return render(request, 'index.html', {'student': student, 'paper': paper, 'grade': grade})
        else:
            messages.error(request, '用户名或密码不正确')
            return render(request, 'login.html', {'message': '密码不正确'})
    elif request.method == 'GET':
        return render(request, 'login.html')
    else:
        return HttpResponse("请使用GET或POST请求数据")


# 首页
def index(request):
    if request.session.get('is_login', None):  # 若session认证为真
        username = request.session.get('username', None)
        # print(username)
        student = models.Student.objects.get(sid=username)
        # 查询考试信息
        paper = models.TestPaper.objects.filter(major=student.major)
        return render(request, 'index.html', {'student': student, 'paper': paper})
    else:
        return render(request, 'index.html')


def userfile(request):
    if request.session.get('is_login', None):  # 若session认证为真
        username = request.session.get('username', None)
        # print(username)
        student = models.Student.objects.get(sid=username)
        # 查询考试信息
        paper = models.TestPaper.objects.filter(major=student.major)
        return render(request, 'userfile.html', {'student': student})


# 学生退出登录
def stulogout(request):
    request.session.clear()
    url = reverse('index')
    return redirect(url)


# 考试信息
def startExam(request):
    sid = request.GET.get('sid')
    title = request.GET.get('title')  # 试卷名字 唯一
    subject1 = request.GET.get('subject')  # 考试科目

    student = models.Student.objects.get(sid=sid)

    # 试卷信息
    paper = models.TestPaper.objects.filter(title=title, course__course_name=subject1)

    pa = models.TestPaper.objects.filter(title=title)

    Testquestions = models.TestquestionBank.objects.filter(Testid=paper[0].id).values('QuestionBankid')

    i = 0
    j = []
    st = 0

    for tq in Testquestions:
        i += 1
        j.append(tq['QuestionBankid'])

    if i == 1:
        q = models.QuestionBank.objects.filter(Q(id=j[0]))
        p = models.QuestionBank.objects.filter(Q(id=j[0])).values('score')
        for m in p:
            st += m['score']

    if i == 2:
        q = models.QuestionBank.objects.filter(Q(id=j[0]) | Q(id=j[1]))
        p = models.QuestionBank.objects.filter(Q(id=j[0]) | Q(id=j[1])).values('score')
        for m in p:
            st += m['score']

    if i == 3:
        q = models.QuestionBank.objects.filter(Q(id=j[0]) | Q(id=j[1]) | Q(id=j[2]))
        p = models.QuestionBank.objects.filter(Q(id=j[0]) | Q(id=j[1]) | Q(id=j[2])).values('score')
        for m in p:
            st += m['score']

    if i == 4:
        q = models.QuestionBank.objects.filter(Q(id=j[0]) | Q(id=j[1]) | Q(id=j[2]) | Q(id=j[3]))
        p = models.QuestionBank.objects.filter(Q(id=j[0]) | Q(id=j[1]) | Q(id=j[2]) | Q(id=j[3])).values('score')
        for m in p:
            st += m['score']

    if i == 5:
        q = models.QuestionBank.objects.filter(Q(id=j[0]) | Q(id=j[1]) | Q(id=j[2]) | Q(id=j[3]) | Q(id=j[4]))
        p = models.QuestionBank.objects.filter(Q(id=j[0]) | Q(id=j[1]) | Q(id=j[2]) | Q(id=j[3]) | Q(id=j[4])).values(
            'score')
        for m in p:
            st += m['score']

    if i == 6:
        q = models.QuestionBank.objects.filter(
            Q(id=j[0]) | Q(id=j[1]) | Q(id=j[2]) | Q(id=j[3]) | Q(id=j[4]) | Q(id=j[5]))
        p = models.QuestionBank.objects.filter(
            Q(id=j[0]) | Q(id=j[1]) | Q(id=j[2]) | Q(id=j[3]) | Q(id=j[4]) | Q(id=j[5])).values('score')
        for m in p:
            st += m['score']
    if i == 7:
        q = models.QuestionBank.objects.filter(
            Q(id=j[0]) | Q(id=j[1]) | Q(id=j[2]) | Q(id=j[3]) | Q(id=j[4]) | Q(id=j[5]) | Q(id=j[6]))
        p = models.QuestionBank.objects.filter(
            Q(id=j[0]) | Q(id=j[1]) | Q(id=j[2]) | Q(id=j[3]) | Q(id=j[4]) | Q(id=j[5]) | Q(id=j[6])).values('score')
        for m in p:
            st += m['score']

    if i == 8:
        q = models.QuestionBank.objects.filter(
            Q(id=j[0]) | Q(id=j[1]) | Q(id=j[2]) | Q(id=j[3]) | Q(id=j[4]) | Q(id=j[5]) | Q(id=j[6]) | Q(id=j[7]))
        p = models.QuestionBank.objects.filter(
            Q(id=j[0]) | Q(id=j[1]) | Q(id=j[2]) | Q(id=j[3]) | Q(id=j[4]) | Q(id=j[5]) | Q(id=j[6]) | Q(
                id=j[7])).values('score')
        for m in p:
            st += m['score']

    if i == 9:
        q = models.QuestionBank.objects.filter(
            Q(id=j[0]) | Q(id=j[1]) | Q(id=j[2]) | Q(id=j[3]) | Q(id=j[4]) | Q(id=j[5]) | Q(id=j[6]) | Q(id=j[7]) | Q(
                id=j[8]))
        p = models.QuestionBank.objects.filter(
            Q(id=j[0]) | Q(id=j[1]) | Q(id=j[2]) | Q(id=j[3]) | Q(id=j[4]) | Q(id=j[5]) | Q(id=j[6]) | Q(
                id=j[7]) | Q(id=j[8])).values('score')
        for m in p:
            st += m['score']

    if i == 10:
        q = models.QuestionBank.objects.filter(
            Q(id=j[0]) | Q(id=j[1]) | Q(id=j[2]) | Q(id=j[3]) | Q(id=j[4]) | Q(id=j[5]) | Q(id=j[6]) | Q(id=j[7]) | Q(
                id=j[8]) | Q(id=j[9]))
        p = models.QuestionBank.objects.filter(
            Q(id=j[0]) | Q(id=j[1]) | Q(id=j[2]) | Q(id=j[3]) | Q(id=j[4]) | Q(id=j[5]) | Q(id=j[6]) | Q(
                id=j[7]) | Q(id=j[8]) | Q(id=j[9])).values('score')
        for m in p:
            st += m['score']
    now_date = timezone.now()
    time_difference = timedelta(minutes=10)

    print(now_date)
    if now_date < paper[0].examtime or now_date >= paper[0].examtime + time_difference:
        messages.error(request, '未到考试时间或考试时间已过')
        return render(request, 'index.html', {'message': '密码不正确'})
    context = {
        'student': student,
        'paper': q,
        'title': title,
        'subject': subject1,
        'count': i,  # 数据表中数据的条数
        'examtime': pa[0].time,
        'score': st

    }
    return render(request, 'exam.html', context=context)


def examinfo(request):
    if request.session.get('is_login', None):
        username = request.session.get('username', None)
        student = models.Student.objects.get(sid=username)
        # 查询成绩信息
        grade = models.Record.objects.filter(sid=student.sid)
        return render(request, 'examinfo.html', {'student': student, 'grade': grade})
    else:
        return render(request, 'examinfo.html')


def calculateGrade(request):
    if request.method == 'POST':

        sid = request.POST.get('sid')
        subject1 = request.POST.get('subject')
        print(subject1)
        title = request.POST.get('title')
        # print(title)
        student = models.Student.objects.get(sid=sid)
        # paper = models.TestPaper.objects.filter(title=title)
        paper = models.TestPaper.objects.filter(major=student.major)
        # print(paper)
        grade = models.Record.objects.filter(sid=student.sid)
        course = models.Course.objects.filter(course_name=subject1).first()
        now = datetime.now()

        Testquestions = models.TestquestionBank.objects.filter(Testid=paper[0].id).values('QuestionBankid')

        i = 0
        j = []

        for tq in Testquestions:
            i += 1
            j.append(tq['QuestionBankid'])

        if i == 1:
            q = models.QuestionBank.objects.filter(Q(id=j[0])).values('id', 'answer', 'score')

        if i == 2:
            q = models.QuestionBank.objects.filter(Q(id=j[0]) | Q(id=j[1])).values('id', 'answer', 'score')

        if i == 3:
            q = models.QuestionBank.objects.filter(Q(id=j[0]) | Q(id=j[1]) | Q(id=j[2])).values('id', 'answer', 'score')

        if i == 4:
            q = models.QuestionBank.objects.filter(Q(id=j[0]) | Q(id=j[1]) | Q(id=j[2]) | Q(id=j[3])).values('id',
                                                                                                             'answer',
                                                                                                             'score')

        if i == 5:
            q = models.QuestionBank.objects.filter(
                Q(id=j[0]) | Q(id=j[1]) | Q(id=j[2]) | Q(id=j[3]) | Q(id=j[4])).values('id', 'answer', 'score')

        if i == 6:
            q = models.QuestionBank.objects.filter(
                Q(id=j[0]) | Q(id=j[1]) | Q(id=j[2]) | Q(id=j[3]) | Q(id=j[4]) | Q(id=j[5])).values('id', 'answer',
                                                                                                    'score')
        if i == 7:
            q = models.QuestionBank.objects.filter(
                Q(id=j[0]) | Q(id=j[1]) | Q(id=j[2]) | Q(id=j[3]) | Q(id=j[4]) | Q(id=j[5]) | Q(id=j[5]) | Q(
                    id=j[6])).values('id', 'answer', 'score')

        if i == 8:
            q = models.QuestionBank.objects.filter(
                Q(id=j[0]) | Q(id=j[1]) | Q(id=j[2]) | Q(id=j[3]) | Q(id=j[4]) | Q(id=j[5]) | Q(id=j[5]) | Q(
                    id=j[6]) | Q(id=j[7])).values('id', 'answer', 'score')

        if i == 9:
            q = models.QuestionBank.objects.filter(
                Q(id=j[0]) | Q(id=j[1]) | Q(id=j[2]) | Q(id=j[3]) | Q(id=j[4]) | Q(id=j[5]) | Q(id=j[5]) | Q(
                    id=j[6]) | Q(id=j[7]) | Q(id=j[8])).values('id', 'answer', 'score')

        if i == 10:
            q = models.QuestionBank.objects.filter(
                Q(id=j[0]) | Q(id=j[1]) | Q(id=j[2]) | Q(id=j[3]) | Q(id=j[4]) | Q(id=j[5]) | Q(id=j[5]) | Q(
                    id=j[6]) | Q(id=j[7]) | Q(id=j[8]) | Q(id=j[9])).values('id', 'answer', 'score')
        stu_grade = 0  # 初始化一个成绩
        for p in q:
            qid = str(p['id'])
            stu_ans = request.POST.get(qid)
            cor_ans = p['answer']
            if stu_ans == cor_ans:
                stu_grade += p['score']
        models.Record.objects.create(sid_id=sid, course_id=course.id, grade=stu_grade, rtime=now)
        context = {
            'student': student,
            'paper': paper,
            'grade': grade
        }
        return render(request, 'index.html', context=context)
