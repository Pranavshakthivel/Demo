from fabric.api import local
import os
import shutil


def cd():
    local('git config --global user.name "Pranavshakthivel"')
    local('git config --global user.email "Pranav.shakthivel@gmail.com"')


def pull():
    local("git pull origin master")


def merge():
    f = open(r"C:\Users\Prakash\PycharmProjects\mark3\new year.txt")
    g = open("C:\\Users\\Prakash\\PycharmProjects\\mark3\\christmas.txt", 'a+')
    text = f.read()
    g.write(text)
    f.close()
    g.close()


def add():
    local("git add .")


def commit():
    n = input("Enter the commit : ")
    local('git commit -m "%s"' % n)


def push():
    local("git push -f origin master")


def tags():
    global t
    t = input("Enter the tag name : ")
    u = input("Enter the message: ")
    local('git tag -a %s -m "%s"' % (t, u))
    local("git push --tags")
    local("git archive --format=zip --output %s.zip %s" % (t, t))


def move():
    c = '%s.zip' % t
    path = 'C:\\Users\\Prakash\\PycharmProjects\\mark3\\'
    moveto = "C:\\Users\\Prakash\\PycharmProjects\\"
    file = os.listdir(path)
    file.sort()
    for f in file:
        if f == c:
            src = path + f
            dst = moveto + f
            shutil.move(src, dst)


def deploy():
    cd()
    pull()
    merge()
    add()
    commit()
    push()
    tags()
    move()
