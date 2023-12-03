import unittest
from unittest.mock import patch
from agents.assistants.assistant_retrevial import *

class TestAssistants(unittest.TestCase):

    def setUp(self):
        self.assistant_id = "assistant_123"
        self.assistant_name = "Test Assistant"
        self.instructions = "Test instructions"
        self.tools = ["tool1", "tool2"]
        self.model = "gpt-3.5-turbo"

    def test_list_assistants(self):
        with patch("openai.beta.assistants.list") as mock_list:
            mock_list.return_value = {"data": [{"id": self.assistant_id, "name": self.assistant_name}]}
            assistants = list_assistants()
            self.assertEqual(assistants, [{"id": self.assistant_id, "name": self.assistant_name}])

    def test_retrieve_assistants_by_name(self):
        with patch("openai.beta.assistants.list") as mock_list:
            mock_list.return_value = {"data": [{"id": self.assistant_id, "name": self.assistant_name}]}
            assistants = retrieve_assistants_by_name(self.assistant_name)
            self.assertEqual(assistants, [{"id": self.assistant_id, "name": self.assistant_name}])

    def test_get_assistant_names(self):
        with patch("openai.beta.assistants.list") as mock_list:
            mock_list.return_value = {"data": [{"id": self.assistant_id, "name": self.assistant_name}]}
            assistant_names = get_assistant_names()
            self.assertEqual(assistant_names, [self.assistant_name])

    def test_delete_assistant(self):
        with patch("requests.delete") as mock_delete:
            mock_delete.return_value.status_code = 200
            delete_assistant(self.assistant_id)
            mock_delete.assert_called_with(f"{BASE_URL}/{self.assistant_id}", headers=HEADERS, timeout=10)

    def test_select_assistant(self):
        with patch("openai.beta.assistants.retrieve") as mock_retrieve:
            mock_retrieve.return_value = {"id": self.assistant_id}
            assistant_id = select_assistant(self.assistant_id)
            self.assertEqual(assistant_id, self.assistant_id)

    def test_create_assistant(self):
        with patch("openai.beta.assistants.create") as mock_create:
            mock_create.return_value = {"id": self.assistant_id}
            assistant_id = create_assistant(self.assistant_name, self.instructions, self.tools, self.model)
            self.assertEqual(assistant_id, self.assistant_id)

    def test_get_assistant_by_id(self):
        with patch("openai.beta.assistants.retrieve") as mock_retrieve:
            mock_retrieve.return_value = {"id": self.assistant_id}
            assistant_id = get_assistant_by_id(self.assistant_id)
            self.assertEqual(assistant_id, self.assistant_id)

    def test_create_thread(self):
        with patch("openai.beta.threads.create") as mock_create:
            mock_create.return_value = {"id": "thread_123"}
            thread = create_thread()
            self.assertEqual(thread, {"id": "thread_123"})

if __name__ == "__main__":
    unittest.main()
