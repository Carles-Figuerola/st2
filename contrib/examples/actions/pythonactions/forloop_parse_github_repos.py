from st2actions.runners.pythonrunner import Action
from bs4 import BeautifulSoup

class ParseGithubRepos(Action):
  def run(self, content):
    try:
      soup = BeautifulSoup(content, 'html.parser')
      repo_list = soup.find_all("h3")
      output = {}
      for each_item in repo_list:
        repo_half_url = each_item.find("a")['href']
        repo_name = repo_half_url.split("/")[-1]
        repo_url = "https://github.com" + repo_half_url
        output[repo_name] = repo_url
    except Exception as e:
      return (False, "Could not parse data: {}".format(e.message))

    return (True, output)
