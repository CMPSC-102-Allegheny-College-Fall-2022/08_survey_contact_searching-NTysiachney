"""Search for an email address given a fragment of a job description."""

from typing import List

import csv

# note: see https://docs.python.org/3/library/csv.html 


def search_for_email_given_job(job_description: str, contacts: str) -> List[List[str]]:
    """Search for and return job description(s) given an email address."""
    # : create an empty list of the contacts
    contact_list = []
    # : iterate through the file, parsing it line by line
    emailReader = csv.reader(contacts.splitlines(), delimiter=',', quotechar='"')
    for contact_line in emailReader: #iterates through CSV
        current_contact_job = contact_line[1] #assigns the value at index 1 to current_contacts_job variable
        if job_description.lower() in current_contact_job.lower() : #if the job descriptions match
            contact_list.append(contact_line) #adds to contact list
    return contact_list


