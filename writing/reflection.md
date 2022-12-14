# Contact Searching

TODO: Make sure that you delete all of the TODO markers and the written prompts
from this document. You should also ensure that the document does not have any
mistakes in spelling, grammar, or the syntax of Markdown. Ultimately, the final
version of your reflection should be a polished document that is suitable for
publication on your web site.

Nick Tysiachney

## Program Output

### What is the output from running the following commands?

TODO: Use a fenced code block to provide the output for this command.

- `poetry run contactsearcher --job-description "engineer" --contacts-file input/contacts.txt`

```
The contacts file contains 100 people in it! Let's get searching!

  We are looking for contacts who have a job related to "engineer":
[
    ['joe70@yahoo.com', 'Network engineer'],
    ['torresjames@white.info', 'Electrical engineer'],
    ['grahamjoel@castillo-gilbert.net', 'Engineer, technical sales'],
    ['gsutton@miller.com', 'Engineer, maintenance'],
    ['gharris@villarreal-snow.com', 'Water engineer'],
    ['williamsondavid@lopez.com', 'Automotive engineer'],
    ['ronald83@yahoo.com', 'Maintenance engineer'],
    ['zmarshall@yahoo.com', 'Control and instrumentation engineer'],
    ['christopher35@yahoo.com', 'Civil engineer, consulting'],
    ['jacquelinedavid@hotmail.com', 'Engineer, electronics'],
    ['espinozadaryl@hill-maddox.com', 'Engineering geologist'],
    ['edwardsjacob@gmail.com', 'Chemical engineer']
]
Wow, we found some contacts! Email them to learn about your job!
```

- `poetry run contactsearcher --job-description "neer" --contacts-file input/contacts.txt`

```
The contacts file contains 100 people in it! Let's get searching!

  We are looking for contacts who have a job related to "neer":
[
    ['joe70@yahoo.com', 'Network engineer'],
    ['torresjames@white.info', 'Electrical engineer'],
    ['grahamjoel@castillo-gilbert.net', 'Engineer, technical sales'],
    ['gsutton@miller.com', 'Engineer, maintenance'],
    ['gharris@villarreal-snow.com', 'Water engineer'],
    ['williamsondavid@lopez.com', 'Automotive engineer'],
    ['ronald83@yahoo.com', 'Maintenance engineer'],
    ['zmarshall@yahoo.com', 'Control and instrumentation engineer'],
    ['christopher35@yahoo.com', 'Civil engineer, consulting'],
    ['jacquelinedavid@hotmail.com', 'Engineer, electronics'],
    ['espinozadaryl@hill-maddox.com', 'Engineering geologist'],
    ['edwardsjacob@gmail.com', 'Chemical engineer']
]
Wow, we found some contacts! Email them to learn about your job!
```

## Source Code and Configuration Files

### Describe in detail how your provided source code works

#### The source code statement that makes the `search` module available to `main`

```
from contactsearcher import search
```

This code imports the search module into main. Since search is localted in the
contactsearcher folder, one must import search from this folder so python knows
where to look for it

#### The source code statement that extracts the current job description for a contact

```
current_contact_job = contact_line[1]
```

This line assigns the value at index position 1 of contact line to a variable
named current_contact_job. Using the code found in the link about csv files, the
csv is converted into a psuedo list. Because of this, simply taking the index
position of the job description (1) allows the program to get the job
description from the csv.

#### Invocation of the function called `search_for_email_given_job`

TODO: Use a fenced code block to provide the requested source code

```
contact = search.search_for_email_given_job(job_description, contacts_text)
```

This code calls the search module and the search_for_email_given_job function
from within that module. It passes in the job description and contact list as
arguments. TODO: Write at least one paragraph to explain the request source code

#### Test case for the function called `search_for_email_given_job`

TODO: Use a fenced code block to provide the requested source code TODO: Write
at least one paragraph to explain the request source code

#### Execute trace of the `contactsearcher` program

TODO: Explain each function call that takes place for the following run of the
program TODO: Write at least one paragraph to explain every function call when
running `contactsearcher`

TODO: Your discussion should start with the invocation of the `contactsearcher`
function in the `main` module, explain all of the subsequent function calls in
the correct order, and then show how the program's control returns to the
`contactsearcher` function in the `main` module.

- `poetry run contactsearcher --job-description "engineer" --contacts-file input/contacts.txt`

## Professional Assessment

### So far this semester, what is one area in which you have struggled? How did you overcome this challenge?

TODO: Provide a one-paragraph response that answers this question in your own
words.

### Based on your experiences with this project, what is one way in which you want to improve?

TODO: Provide a one-paragraph response that answers this question in your own
words.
