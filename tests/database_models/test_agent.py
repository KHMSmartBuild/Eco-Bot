# tests/test_agent.py
"""
Test case for the agents table in the database.
"""
import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from data.database.utils.db_operations import Base, Agent

class AgentModelTestCase(unittest.TestCase):
    """
    Test case for the Agent model.
    """
    @classmethod
    def setUpClass(cls):
        """
        Set up the class by creating an in-memory database using SQLite 
        and creating all the tables defined in the metadata.
        """
        cls.engine = create_engine('sqlite:///:memory:')  # Create an in-memory database
        Base.metadata.create_all(cls.engine)
        cls.Session = scoped_session(sessionmaker(bind=cls.engine))

    @classmethod
    def tearDownClass(cls):
        """
        Tear down the class after running all test methods.

        This method is called once after all test methods in the class have been run.
        It is responsible for removing the session and dropping all metadata from the engine.

        Parameters:
            cls (class object): The class object.

        Returns:
            None
        """
        cls.Session.remove()
        Base.metadata.drop_all(cls.engine)

    def setUp(self):
        """
        Set up the test case by initializing the session.
        """
        self.session = self.Session()

    def tearDown(self):
        """
        Tears down the test case by rolling back the session.

        This function does not take any parameters.

        This function does not return anything.
        """
        self.session.rollback()

    def test_agent_creation(self):
        """
        Test the creation of an agent.

        This function creates an instance of the Agent class using the provided parameters
        and performs the necessary database operations to persist the agent object.
        It then asserts that the agent's ID is not None.

        Parameters:
            self (object): The current instance of the test class.
        
        Returns:
            None
        
        Raises:
            AssertionError: If the agent's ID is None.
        """
        agent = Agent('Type1', 'AgentName', ...)  # Fixed the positional argument placement
        self.session.add(agent)
        self.session.commit()
        self.assertIsNotNone(agent.agentid)
        # Additional test assertions

if __name__ == '__main__':
    unittest.main()
