import jenkins
server = jenkins.Jenkins('http://localhost:8080', username='admin', password='admin')
user = server.get_whoami()
version = server.get_version()
print('Chatbot Automation %s Version: %s' % (user['fullName'], version))

jenkins_jobs = server.get_jobs()
print jenkins_jobs
jenkins_jobs = server.get_job_config('chatbot-aem')
print(jenkins_jobs)
server.build_job('chatbot-aem')