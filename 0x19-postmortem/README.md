# Postmortem

![funny-simpsons-gif-t04h-u77r6xxshkziwh4vq.gif](Postmortem%20d1efdc3a388f416c8bcd7d09abb2b3ed/funny-simpsons-gif-t04h-u77r6xxshkziwh4vq.gif)

- Issue Summary:
    
    On April 15th, 2022 at 13:00 GMT+0 the “Stagiaire” e-learning platform couldn’t see there progress even if they can log in to it due to problem with our API which resulted 9 errors, because the API address was mess typed.
    
- Timeline:
    - at 13:00 GMT+0 : the issue was detected and reported by many users.
    - at 13:10 GMT+0 : making sure our API is working as expected using Postman.
    - at 13:14 GMT+0 : API checked and everything working as expected and moved to check the code base.
    - at 13:48 GMT+0: the issue was fond a missed type API link
    - at 13:55 GMT+0 : the solution was pushed after being tested.
- Root cause and resolution must contain:
    - one of the team members pushed a feature to the production without testing.
    - the problem fixed after noticing the problem we solve it and run multiple tests and pushed the solution.
- Corrective and preventative measures must contain:

![vsgif_com__.1992304.gif](Postmortem%20d1efdc3a388f416c8bcd7d09abb2b3ed/vsgif_com__.1992304.gif)

**Code review:**

1. **Write clear and concise commit messages.** This will help your reviewers to understand what changes you have made and why.
2. **Push your changes to a branch and create a merge request.** This will allow your reviewers to easily review your changes and provide feedback.
3. **Ask peers and colleagues to review your code.** When choosing reviewers, consider the following factors:
    - Experience with the codebase
    - Expertise in the area of code you are changing
    - Fresh perspective
4. **Respond to feedback promptly.** Be open to feedback and make changes to your code as needed.
5. **Once your code has been approved, merge your branch into the main codebase.**

**Testing:**

1. **Write comprehensive unit tests.** Unit tests test individual units of code, such as functions, classes, and modules.
2. **Write integration tests.** Integration tests test how different units of code work together.
3. **Write end-to-end tests.** End-to-end tests test the entire application from start to finish.
4. **Run your tests in a variety of environments and scenarios.** This will help to ensure that your code works as expected in production.
