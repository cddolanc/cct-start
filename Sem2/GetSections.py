from requests import get, post

# Module variables to connect to moodle api:
## Insert token and URL for your site here. 
## Mind that the endpoint can start with "/moodle" depending on your installation.
KEY = "8cc87cf406775101c2df87b07b3a170d" 
URL = "https://034f8a1dcb5c.eu.ngrok.io"
ENDPOINT="/webservice/rest/server.php"

def rest_api_parameters(in_args, prefix='', out_dict=None):
    """Transform dictionary/array structure to a flat dictionary, with key names
    defining the structure.
    Example usage:
    >>> rest_api_parameters({'courses':[{'id':1,'name': 'course1'}]})
    {'courses[0][id]':1,
     'courses[0][name]':'course1'}
    """
    if out_dict==None:
        out_dict = {}
    if not type(in_args) in (list,dict):
        out_dict[prefix] = in_args
        return out_dict
    if prefix == '':
        prefix = prefix + '{0}'
    else:
        prefix = prefix + '[{0}]'
    if type(in_args)==list:
        for idx, item in enumerate(in_args):
            rest_api_parameters(item, prefix.format(idx), out_dict)
    elif type(in_args)==dict:
        for key, item in in_args.items():
            rest_api_parameters(item, prefix.format(key), out_dict)
    return out_dict

def call(fname, **kwargs):
    """Calls moodle API function with function name fname and keyword arguments.
    Example:
    >>> call_mdl_function('core_course_update_courses',
                           courses = [{'id': 1, 'fullname': 'My favorite course'}])
    """
    parameters = rest_api_parameters(kwargs)
    parameters.update({"wstoken": KEY, 'moodlewsrestformat': 'json', "wsfunction": fname})
    #print(parameters)
    response = post(URL+ENDPOINT, data=parameters).json()
    if type(response) == dict and response.get('exception'):
        raise SystemError("Error calling Moodle API\n", response)
    return response

################################################
# Rest-Api classes
################################################

class LocalGetSections(object):
    """Get settings of sections. Requires courseid. Optional you can specify sections via number or id."""
    def __init__(self, cid, secnums = [], secids = []):
        self.getsections = call('local_wsmanagesections_get_sections', courseid = cid, sectionnumbers = secnums, sectionids = secids)

################################################
# Example
################################################

courseid = "12" # Exchange with valid id.
# # Get all sections of the course.
sec = LocalGetSections(courseid)
# # Get sections ids of the course with the given numbers.
# # sec = LocalGetSections(courseid, [0, 1, 2, 3, 5, 6])
# # # Get sections ids of the course with the given ids.
# # sec = LocalGetSections(courseid, [], [7186, 7187, 7188, 7189])
# # # Get sections ids of the course with the given numbers and given ids.
# # sec = LocalGetSections(courseid, [0, 1, 2, 3, 5, 6], [7186, 7187, 7188, 7189])
print(sec.getsections)






# Takes a dictionary of links to Moodle pages and returns a dictionary
# of download links to all of the PDF files on those pages
# def get_links(session, page_links):
#     links_to_pdfs = {}
#     for subject in page_links:
#         html = session.get(page_links[subject]).text
#         soup = BeautifulSoup(html, "lxml")
#         data = soup.find_all("li", attrs={"class": "activity resource"})
#         links_to_pdfs[subject] = {}
#         dup = 0 # Count duplicate file names to prevent overwriting dictionary values

#         # Store PDF links in a dictionary
#         for li in data:
#             links = li.find_all("a")
#             for a in links:
#                 if "PDF document" in a.text:
#                     doc_name = a.text.replace(" PDF document", "")
#                     if doc_name in links_to_pdfs[subject]:
#                         dup += 1
#                         links_to_pdfs[subject][doc_name + "_" + str(dup)] = a["href"]
#                     else:
#                         links_to_pdfs[subject][doc_name] = a["href"]

#     return links_to_pdfs

#     print(get_links)