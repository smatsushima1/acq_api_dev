# https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask

import flask
from flask import request, jsonify

# allow errors to show in the app
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# sample data
cit_dev = [
  {
    "citation": "1.000",
    "part": "1",
    "subpart": "1",
    "section": "0",
    "sub-section": "",
    "title": "Scope of Part.",
    "text_html": "<p>This part sets forth basic policies and general information about the Federal Acquisition Regulations System including purpose, authority, applicability, issuance, arrangement, numbering, dissemination, implementation, supplementation, maintenance, administration, and deviation. subparts  1.2,1.3, and 1.4 prescribe administrative procedures for maintaining the FAR System.</p>"
  },
  {
    "citation": "1.101",
    "part": "1",
    "subpart": "1",
    "section": "1",
    "sub-section": "",
    "title": "Purpose.",
    "text_html": "<p>The Federal Acquisition Regulations System is established for the codification and publication of uniform policies and procedures for acquisition by all executive agencies. The Federal Acquisition Regulations System consists of the Federal Acquisition Regulation (FAR), which is the primary document, and agency acquisition regulations that implement or supplement the FAR. The FAR System does not include internal agency guidance of the type described in 1.301(a)(2).</p>"
  },
  {
    "citation": "1.102",
    "part": "1",
    "subpart": "1",
    "section": "2",
    "sub-section": "",
    "title": "Statement of guiding principles for the Federal Acquisition System.",
    "text_html": "<ul><li>(a) The vision for the Federal Acquisition System is to deliver on a timely basis the best value product or service to the customer, while maintaining the public’s trust and fulfilling public policy objectives. Participants in the acquisition process should work together as a team and should be empowered to make decisions within their area of responsibility.</li><br><li>(b) The Federal Acquisition System will-</li><br><ul><li>(1) Satisfy the customer in terms of cost, quality, and timeliness of the delivered product or service by, for example-</li><br><ul><li>(i) Maximizing the use of commercial products and services;</li><br><li>(ii) Using contractors who have a track record of successful past performance or who demonstrate a current superior ability to perform; and</li><br><li>(iii) Promoting competition;</li><br></ul><li>(2) Minimize administrative operating costs;</li><br><li>(3) Conduct business with integrity, fairness, and openness; and</li><br><li>(4) Fulfill public policy objectives.</li><br></ul><li>(c) The Acquisition Team consists of all participants in Government acquisition including not only representatives of the technical, supply, and procurement communities but also the customers they serve, and the contractors who provide the products and services.</li><br><li>(d) The role of each member of the Acquisition Team is to exercise personal initiative and sound business judgment in providing the best value product or service to meet the customer’s needs. In exercising initiative, Government members of the Acquisition Team may assume if a specific strategy, practice, policy or procedure is in the best interests of the Government and is not addressed in the FAR, nor prohibited by law (statute or case law), Executive order or other regulation, that the strategy, practice, policy or procedure is a permissible exercise of authority.</li><br></ul>"
       }
       ]

# home page
@app.route('/', methods=['GET'])
def home():
  return """
<h1>FAR</h1>
<p>This will house the FAR.</p>
"""

# url location for all the results
@app.route('/api/far/1', methods=['GET'])
def api_all():
  return jsonify(cit_dev)

# filtering capabilities
@app.route('/api/far', methods=['GET'])
def api_cit():
  # check if a citation was provided as part of the URL
  # if provided, assign it to a variable
  # if not, display an error
  if 'citation' in request.args:
    cit = str(request.args['citation'])
  else:
    return "Error: No citation provided. Please specify a citation."

  # create an empty list for our results
  results = []

  # loop through the data and match results that fit the requested citation
  # citations are unique, but other fields might return many results
  for i in cit_dev:
    if i['citation'] == cit:
      results.append(i)

  # use the jsonify function from Flask to convert our list to the JSON format
  return jsonify(results)

app.run()

