import unittest
from app.models import Pitch,User
from app import db



class PitchTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the  class
    '''
          
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.user_Dev = User(username = 'Levy',password = 'developer', email = 'Levy@dev.com')
          
        self.new_pitch = Pitch(title='Humour',pitch="My Dad once told me, 'While you're out buy milk.' I never went back.",category="Humour",user = self.user_Dev)
   
    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))
  
    
    # We then check if the values of variables are correctly being placed.
    def test_check_instance_variables(self):
        
        self.assertEquals(self.new_pitch.title,'Humour')
        self.assertEquals(self.new_pitch.pitch,"My Dad once told me, 'While you're out buy milk.' I never went back.")
        self.assertEquals(self.new_pitch.category,'Humour')
        self.assertEquals(self.new_pitch.user,self.user_Dev)
       
    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)
        
   
    def test_get_pitch_by_category(self):

        self.new_pitch.save_pitch()
        got_pitches = Pitch.get_pitches("Humour")
        self.assertTrue(len(got_pitches) > 0)

 
