#!/home/student/Frank/OpenAPS-Glucosym-3.9/venv/bin/python
# PYTHON_ARGCOMPLETE_OK

from decocare.helpers import messages

if __name__ == '__main__':
  app = messages.SendMsgApp( )
  app.run(None)

