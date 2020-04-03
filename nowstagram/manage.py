# -*- encoding=UTF-8 -*-

from nowstagram import app, db
from flask_script import Manager
from sqlalchemy import or_, and_
from nowstagram.models import User, Image, Comment
import random

manager = Manager(app)


def get_image_url():
    return 'http://images.nowcoder.com/head/' + str(random.randint(0, 1000)) + 'm.png'


@manager.command
def init_database():
    db.drop_all()
    db.create_all()
    for i in range(0, 100):
        db.session.add(User('牛客' + str(i), 'a' + str(i)))

        for j in range(0, 10):  # 每人发十张图
            db.session.add(Image(get_image_url(), i + 1))
            for k in range(0, 3):
                db.session.add(Comment('这是一条评论' + str(k), 1 + 10 * i + j, i + 1))
    db.session.commit()

    # '''
    # 更新
    for i in range(0, 100, 3):
        # 通过update函数
        User.query.filter_by(id=i).update({'username': '33牛客新' + str(i)})

    # User.query.filter(User.username.endswith('0')).update({'username': '00新' + User.username}, synchronize_session=False)
    # filter_by多个参数是and
    User.query.filter_by(id=4, password='a4').update({'username': '44牛客新' + str(i)})
    User.query.filter_by(id=5, password='a4').update({'username': '55牛客新' + str(i)})

    for i in range(7, 100, 10):
        # 通过设置属性
        u = User.query.get(i)
        u.username = '77' + str(i * i)
    db.session.commit()

    # 删除
    for i in range(50, 100, 2):
        Comment.query.filter_by(id=i + 1).delete()
    for i in range(51, 100, 2):
        comment = Comment.query.get(i + 1)
        db.session.delete(comment)
    db.session.commit()

    print(User.query.all())


#  print 2, User.query.get(3) # primary key = 3
#  print 3, User.query.filter_by(id=2).first()
#  print 4.1, User.query.order_by(User.id.desc()).offset(1).limit(2).all()
#  print 4.2, User.query.order_by(db.asc('id')).offset(1).limit(2).all()
#  #print 4.3, User.query.order_by('-id').offset(1).limit(2).all()
#  print 5, User.query.paginate(page=1, per_page=10).items
#  u = User.query.get(1)
#  print 6, u
#  print 7, u.images.all()
#  print 8, Image.query.get(1).user
#  # filter filter_by 区别，表达式和赋值
#  print 9, User.query.filter(User.username.endswith('0')).limit(2).all()
#  print 10, User.query.filter(or_(User.id == 88, User.id == 99)).all()
#  print 11, User.query.filter((User.id == 66) | (User.id == 77)).all()
#  print 12, User.query.filter(and_(User.id > 88, User.id > 99)).limit(10).all()
#  print 13, User.query.filter((User.id == 66) & (User.id < 77)).all()
#  print 14, User.query.filter(User.id.in_((55, 44))).all()
#  #print 7, User.query.get(1).images.filter_by(id=1).first() # Base query:User.query.get(1).images
#  #print User.query.filter_by(id=2).first_or_404()
#  print 15, Comment.query.filter(Comment.id.in_((33, 44))).all()
#  Comment.query.filter(Comment.id.in_((33, 44))).delete(synchronize_session=False)
#  db.session.commit()
#  print 16, Comment.query.filter(Comment.id.in_((33, 44))).all()

if __name__ == '__main__':
    manager.run()
