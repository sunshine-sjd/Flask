from . import db


class Role(db.Model):
    __tablename__ = 'role_table'
    id = db.Column(db.Integer, primary_key=True)
    RoleName = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role: %r>' % self.RoleName


class User(db.Model):
    __tablename__ = 'user_table'
    id = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role_table.id'))

    def __repr__(self):
        return '<User: %r>' % self.UserName

