import os
from flask_mod.app import create_app, db
from flask_mod.app.models import User, Role
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test_flask_web():
    """  unittest is running now!  """
    import unittest
    test123 = unittest.TestLoader().discover(r"flask_mod\tests")
    unittest.TextTestRunner(verbosity=2).run(test123)

if __name__ == '__main__':
    manager.run()
