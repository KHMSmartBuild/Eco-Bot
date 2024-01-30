# db_operations.py
"""
db_operations.py is a file that contains all the database operations for the Agent_DB.
each table in the database is mapped to a class in the db_operations.py file.
"""
from sqlalchemy import Column, Integer, String, ForeignKey, MetaData
from sqlalchemy import TIMESTAMP, JSON, Boolean, Text
from data.database.utils.setconn import session, Base, engine
from logging import getLogger, StreamHandler, INFO, Formatter, FileHandler, basicConfig


# Create a logger object
logger = getLogger(__name__)
logger.setLevel(INFO)
basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create handlers
console_handler = StreamHandler()
file_handler = FileHandler('db_operations.log')
console_handler.setLevel(INFO)
file_handler.setLevel(INFO)

# Create formatters and add it to handlers
console_formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)
file_handler.setFormatter(file_formatter)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Create a session object
conn = session(Base, engine)

class BaseCRUD:
    """
    Base class for CRUD operations.
    """
    __abstract__ = True  # Indicates that BaseCRUD is an abstract class

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def create(self, session: conn, **kwargs) -> None:
        """
        Create a new instance of the class and add it to the session.

        Args:
            session (Session): The session object to add the instance to.
            **kwargs: The keyword arguments used to initialize the instance.

        Returns:
            The newly created instance.
        """
        instance = self.__class__(kwargs=str(kwargs))
        session.add(instance)
        session.commit()
        session.refresh(instance)
        logger.info("Created record: %s", instance)
        return instance

    @classmethod
    def read(cls, session: conn, record_id: int):
        """
        Read a record from the database based on the given id.

        :param session: The session object to use for the database query.
        :type session: Session
        :param id: The id of the record to retrieve.
        :type id: int
        :return: The first record found with the given id, or None if no record is found.
        :rtype: object
        """
        logger.info("Reading record: %s", record_id, extra={'record_id': record_id})
        return session.query(cls).filter_by(record_id=record_id).first()


    @classmethod
    def update(cls, session: conn, record_id: int, **kwargs):
        """
        Updates an existing record in the database with the given kwargs.

        Args:
            session (Session): The database session.
            record_id (int): The ID of the record to be updated.
            **kwargs: Variable keyword arguments for the record attributes to be updated.

        Returns:
            instance: The updated instance of the record if it exists, otherwise None.
        """
        instance = session.query(cls).filter_by(record_id=record_id).first()
        if instance:
            for attr, value in kwargs.items():
                setattr(instance, attr, value)
            session.commit()
            logger.info("Updated record: %s", instance, extra={'record_id': record_id})
            return instance
        else:
            # handle the case where the record does not exist
            pass


    @classmethod
    def delete(cls, session: conn, record_id: int):
        """
        Delete a record by its ID.

        Args:
            session (Session): The database session.
            record_id (int): The ID of the record to be deleted.
        """
        instance = session.query(cls).filter_by(record_id=record_id).first()
        if instance:
            session.delete(instance)
            session.commit()
            logger.info("Deleted record: %s", instance, extra={'record_id': record_id})
            print("Deleted record:", instance)
        else:
            # handle the case where the record does not exist
            pass



class Agent(Base, BaseCRUD):
    """
    This class represents the agents table in the database.
    """
    __tablename__ = 'agents'
    # Add your columns here, for example:
    agentid = Column(Integer, primary_key=True)
    agenttype = Column(String(255))
    name = Column(String(50))
    initializationtime = Column(TIMESTAMP)
    expirytime = Column(TIMESTAMP)
    dockerimageid = Column(Integer, ForeignKey('dockerimages.imageid'))
    container_id = Column(Integer, ForeignKey('containers.container_id'))
    agent_metadata = Column(JSON)
    status = Column(String(255))  
    lastupdated = Column(TIMESTAMP(timezone=True))  


    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete


class AgentProfile(Base, BaseCRUD):
    """
    This class represents the agent_profiles table in the database.
    """
    __tablename__ = 'agent_profiles'
    # Add your columns here, for example:
    profile_id = Column(Integer, primary_key=True)
    agent_id = Column(Integer, ForeignKey('agents.agent_id'))
    capabilities = Column(JSON)
    assigned_tasks = Column(JSON)
    profile_status = Column(Boolean)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete

class AgentFunction(Base, BaseCRUD):
    """
    This class represents the agent_functions table in the database.
    """
    __tablename__ = 'agentfunctions'
    # Add your columns here, for example:
    functionid = Column(Integer, primary_key=True)
    agentname = Column(String(255))
    inputparameters = Column(JSON)
    outputformat = Column(JSON)
    executionfreq = Column(Integer)

    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete


class AgentAPICall(Base, BaseCRUD):
    """
    This class represents the agent_api_calls table in the database.
    """
    __tablename__ = 'agent_api_calls'
    # Add your columns here, for example:
    api_call_id = Column(Integer, primary_key=True)
    agent_id = Column(Integer, ForeignKey('agents.agent_id'))
    api_endpoint = Column(String(255))
    call_time = Column(TIMESTAMP)
    response_status = Column(Integer)

    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete


class AgentGroupChatAssociation(Base, BaseCRUD):
    """
    This class represents the agent_group_chat_association table in the database.
    """
    __tablename__ = 'agent_group_chat_association'
    # Add your columns here, for example:
    agent_id = Column(Integer, ForeignKey('agents.agent_id'), primary_key=True)
    chat_id = Column(Integer, ForeignKey('group_chats.chat_id'), primary_key=True)

    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete

class Assistant(Base, BaseCRUD):
    """
    This class represents the assistants table in the database.
    """
    __tablename__ = 'assistants'
    # Add your columns here, for example:
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    role = Column(String(255))

    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete

class Container(Base, BaseCRUD):
    """
    This class represents the containers table in the database.
    """
    __tablename__ = 'containers'
    # Add your columns here, for example:
    container_id = Column(Integer, primary_key=True)
    container_name = Column(String(255), nullable=False)
    resources = Column(JSON)
    status = Column(String(255), nullable=False)

    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete


class ConversationThread(Base, BaseCRUD):
    """
    This class represents the conversation_threads table in the database.
    """
    __tablename__ = 'conversation_threads'
    # Add your columns here, for example:
    ThreadID = Column(Integer, primary_key=True)
    AgentsInvolved = Column(JSON)
    StartTime = Column(TIMESTAMP)
    Status = Column(String(255))

    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete

class DebugInfo(Base, BaseCRUD):
    """
    This class represents the debug_info table in the database.
    """
    __tablename__ = 'debug_info'
    # Add your columns here, for example:
    debug_id = Column(Integer, primary_key=True)
    timestamp = Column(TIMESTAMP)
    file_name = Column(String(255))
    function_name = Column(String(255))
    line_number = Column(Integer)
    message = Column(String(255))
    
    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete

class DockerImage(Base, BaseCRUD):
    """
    This class represents the docker_images table in the database.
    """
    __tablename__ = 'dockerimages'
    imageid = Column(Integer, primary_key=True)
    imagename = Column(String(255))
    baseos = Column(String(50))
    lastupdate = Column(TIMESTAMP)

    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete

class ExternalAPI(Base, BaseCRUD):
    """
    This class represents the external_apis table in the database.
    """
    __tablename__ = 'external_apis'
    # Add your columns here, for example:
    api_id = Column(Integer, primary_key=True)
    api_name = Column(String(255))
    api_key = Column(String(255))
    base_url = Column(String(255))
    usage_count = Column(Integer)
    last_used = Column(TIMESTAMP)

    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete

class GBTSPrompt(Base, BaseCRUD):
    """
    This class represents the gbts_prompts table in the database.
    """
    __tablename__ = 'gbts_prompts'
    # Add your columns here, for example:
    prompt_id = Column(Integer, primary_key=True)
    template = Column(JSON)
    description = Column(String(255))

    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete

class GBTSResponse(Base, BaseCRUD):
    """
    This class represents the gbts_responses table in the database.
    """
    __tablename__ = 'gbts_responses'
    # Add your columns here, for example:
    response_id = Column(Integer, primary_key=True)
    prompt_id = Column(Integer, ForeignKey('gbts_prompts.prompt_id'))
    agent_id = Column(Integer, ForeignKey('agents.agent_id'))
    response = Column(JSON)
    response_time = Column(TIMESTAMP)

    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete

class GroupChat(Base, BaseCRUD):
    """
    This class represents the group_chats table in the database.
    """
    __tablename__ = 'group_chats'
    # Add your columns here, for example:
    chat_id = Column(Integer, primary_key=True)
    chat_name = Column(String(255), nullable=False)
    start_time = Column(TIMESTAMP)
    status = Column(String(255), nullable=False)

    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete


class Message(Base, BaseCRUD):
    """
    This class represents the messages table in the database.
    """
    __tablename__ = 'messages'
    # Add your columns here, for example:
    messageid = Column(Integer, primary_key=True)
    threadid = Column(Integer, ForeignKey('conversation_threads.threadid'))
    agentid = Column(Integer, ForeignKey('agents.agentid'))
    content = Column(Text)
    timestamp = Column(TIMESTAMP)

    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete

class Project(Base, BaseCRUD):
    """
    This class represents the projects table in the database.
    """
    __tablename__ = 'projects'
    # Add your columns here, for example:
    project_id = Column(Integer, primary_key=True)
    project_name = Column(String(255), nullable=False)
    description = Column(String(255))
    start_date = Column(TIMESTAMP)
    end_date = Column(TIMESTAMP)
    status = Column(Boolean, nullable=False)

    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete

class Run(Base, BaseCRUD):
    """
    This class represents the runs table in the database.
    """
    __tablename__ = 'runs'
    # Add your columns here, for example:
    id = Column(Integer, primary_key=True)
    thread_id = Column(Integer, ForeignKey('threads.id'))
    status = Column(String(255))

    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete

class SystemLog(Base, BaseCRUD):
    """
    This class represents the system_logs table in the database.
    """
    __tablename__ = 'system_logs'
    # Add your columns here, for example:
    log_id = Column(Integer, primary_key=True)
    timestamp = Column(TIMESTAMP)
    log_level = Column(String(255))
    service_name = Column(String(255))
    message = Column(String(255))

    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete

class Task(Base, BaseCRUD):
    """
    This class represents the tasks table in the database.
    """
    __tablename__ = 'tasks'
    # Add your columns here, for example:
    taskid = Column(Integer, primary_key=True)
    description = Column(Text)
    assignedto = Column(String(255), nullable=False)
    status = Column(String(255))
    assigned_agent_id = Column(Integer, ForeignKey('agents.agentid'))

    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete

class TaskHistory(Base, BaseCRUD):
    """
    This class represents the task_history table in the database.
    """
    __tablename__ = 'task_history'
   # Add your columns here, for example:
    history_id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey('tasks.taskid'))
    status_changed_to = Column(String(255))
    change_timestamp = Column(TIMESTAMP)

    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete

class TaskStatus(Base, BaseCRUD):
    """
    This class represents the task_status table in the database.
    """
    __tablename__ = 'task_status'
    # Add your columns here, for example:
    status_id = Column(Integer, primary_key=True)
    status_name = Column(String(255), nullable=False)

    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete

class TaskPriority(Base, BaseCRUD):
    """
    This class represents the task_priority table in the database.
    """
    __tablename__ = 'task_priority'
    # Add your columns here, for example:
    priority_id = Column(Integer, primary_key=True)
    priority_level = Column(String(255), nullable=False)

    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete

class Thread(Base, BaseCRUD):
    """
    This class represents the threads table in the database.
    """
    __tablename__ = 'threads'
    # Add your columns here, for example:
    id = Column(Integer, primary_key=True)
    assistant_id = Column(Integer, ForeignKey('assistants.id'))
    title = Column(String(255))

    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete

class User(Base, BaseCRUD):
    """
    This class represents the users table in the database.
    """
    __tablename__ = 'users'
    # Add your columns here, for example:
    user_id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP)
    user_status = Column(String(255), nullable=False)
    threads = Column(JSON)
    chat = Column(JSON)

    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete

class Websocket(Base, BaseCRUD):
    """
    This class represents the websockets table in the database.
    """
    __tablename__ = 'websockets'
    # Add your columns here, for example:
    socket_id = Column(Integer, primary_key=True)
    endpoint = Column(String(255))
    assoceated_agent = Column(Integer, ForeignKey('agents.agent_id'))
    protocol = Column(String(255))

    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete

class CacheData(Base, BaseCRUD):
    """
    This class represents the cache_data table in the database.
    """
    __tablename__ = 'cache_data'
    # Add your columns here, for example:
    cache_id = Column(Integer, primary_key=True)
    cache_key = Column(String(255))
    cache_value = Column(JSON)
    expiry_time = Column(TIMESTAMP)

    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete

class DigitalTwin(Base, BaseCRUD):
    """
    This class represents the digital_twins table in the database.
    """
    __tablename__ = 'digital_twins'
    # Add your columns here, for example:
    twin_id = Column(Integer, primary_key=True)
    agent_id = Column(Integer, ForeignKey('agents.agentid'))
    twin_data = Column(JSON)
    created_at = Column(TIMESTAMP)
    last_synced = Column(TIMESTAMP)

    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete

class ChatMetadata(Base, BaseCRUD):
    """
    This class represents the chat_metadata table in the database.
    """
    __tablename__ = 'chat_metadata'
    # Add your columns here, for example:
    chat_id = Column(Integer, ForeignKey('group_chats.chat_id'))
    topic = Column(String(255))
    creation_time = Column(TIMESTAMP)
    purpose = Column(String(255))
    
    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete

class ChatHistory(Base, BaseCRUD):
    """
    This class represents the chat_history table in the database.
    """
    __tablename__ = 'chat_history'
    # Add your columns here, for example:
    history_id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, ForeignKey('group_chats.chat_id'))
    message_id = Column(Integer, ForeignKey('messages.messageid'))
    timestamp = Column(TIMESTAMP)

    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete

class ChatSetting(Base, BaseCRUD):
    """
    This class represents the chat_settings table in the database.
    """
    __tablename__ = 'chat_settings'
    # Add your columns here, for example:
    setting_id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, ForeignKey('group_chats.chat_id'))
    settings_data = Column(JSON)

    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete

class ChatVisualizationData(Base, BaseCRUD):
    """
    This class represents the chat_visualization_data table in the database.
    """
    __tablename__ = 'chat_visualization_data'
    # Add your columns here, for example:
    data_id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, ForeignKey('group_chats.chat_id'))
    response_id = Column(Integer, ForeignKey('responses.response_id'))
    visualization_data = Column(JSON)

    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete

class CodeExecution(Base, BaseCRUD):
    """
    This class represents the code_executions table in the database.
    """
    __tablename__ = 'code_executions'
    # Add your columns here, for example:
    executionid = Column(Integer, primary_key=True)
    agentid = Column(Integer, ForeignKey('agents.agent_id'))
    threadid = Column(Integer, ForeignKey('conversation_threads.threadid'))
    codeblock = Column(JSON)
    result = Column(JSON)
    executiontime = Column(TIMESTAMP)

    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete

class ResourceLimit(Base, BaseCRUD):
    """
    This class represents the resource_limits table in the database.
    """
    __tablename__ = 'resource_limits'
    # Add your columns here, for example:
    limit_id = Column(Integer, primary_key=True)
    resource_type = Column(String(255))
    max_limit = Column(Integer)

    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete

class ResourceUsage(Base, BaseCRUD):
    """
    This class represents the resource_usage table in the database.
    """
    __tablename__ = 'resource_usage'
    # Add your columns here, for example:
    usage_id = Column(Integer, primary_key=True)
    agent_id = Column(Integer, ForeignKey('agents.agent_id'))
    resource_type = Column(String(255))
    current_usage = Column(JSON)

    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete

class UserPreference(Base, BaseCRUD):
    """
    This class represents the user_preferences table in the database.
    """
    __tablename__ = 'user_preferences'
    # Add your columns here, for example:
    preference_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    preferences_data = Column(JSON)

    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete


class Rule(Base, BaseCRUD):
    """
    This class represents the rules table in the database.
    """
    __tablename__ = 'rules'
    # Add your columns here, for example:
    ruleid = Column(Integer, primary_key=True)
    rulename = Column(String(255), nullable=False)
    ruledescription = Column(Text)
    priority = Column(Integer)

    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete

class Tool(Base, BaseCRUD):
    """
    This class represents the tools table in the database.
    """
    __tablename__ = 'tools'
    # Add your columns here, for example:
    tool_id = Column(Integer, primary_key=True)
    tool_name = Column(String(255), nullable=False)
    tool_description = Column(Text)
    tool_resource_requirements = Column(JSON)

    # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete

class ContainerTool(Base, BaseCRUD):
    """
    This class represents the container_tools table in the database.
    """
    __tablename__ = 'container_tools'
    # Add your columns here, for example:
    container_id = Column(Integer, ForeignKey('containers.container_id'), primary_key=True)
    tool_id = Column(Integer, ForeignKey('tools.tool_id'), primary_key=True)

        # Define the CRUD methods here
    create = BaseCRUD.create
    read = BaseCRUD.read
    update = BaseCRUD.update
    delete = BaseCRUD.delete

Base.metadata.create_all(engine)
