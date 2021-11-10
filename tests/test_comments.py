import unittest
from app.models import Comment,Pitch,User
from app import db

class CommentsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the class
    '''

    def setUp(self):
        self.user_Dev = User(username='Levy', password='developer', email='Levy@dev.com')  
        self.new_pitch = Pitch(title='Humour',pitch="My Dad once told me, 'While you're out buy milk.' I never went back.",category="Humour",user = self.user_Dev)
        self.new_comment= Comment(comment="Hahaha, so the loop continues...great pitch!",user=self.user_Dev,pitch=self.new_pitch)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()
        Comment.query.delete()
        
        
    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'Hahaha, so the loop continues...great pitch!')
        self.assertEquals(self.new_comment.user,self.user_Dev)
        self.assertEquals(self.new_comment.pitch,self.new_pitch)


    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all()) > 0)
