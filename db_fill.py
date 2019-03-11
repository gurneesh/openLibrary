# -*- coding: utf-8 -*-

from app import app, db
from app.models import User, Book, Log, Role

app_ctx = app.app_context()
app_ctx.push()
db.create_all()
Role.insert_roles()

admin = User(name=u'root', email='root@gmail.com', password='password', major='administrator',
             headline=u"Temporary administrator", about_me=u"Graduated from the Department of Management and is interested in reading, so part-time librarian.")
user1 = User(name=u'Akalin', email='akarin@gmail.com', password='123456', major='Computer Science', headline=u"Ordinary student")
user2 = User(name=u'test', email='test@test.com', password='123456')
user3 = User(name=u'gurneesh', email='gurneesh@email.com', password='123456')
user4 = User(name=u'gurn33sh', email='gurn33sh@email.com', password='123456')

book1 = Book(title=u"Flask Web Development", subtitle=u"based on Python for Web Application development framework", author=u"Miguel Grinberg", isbn='9787115373991',
             tags_string=u"Computer, programming, web development", image='Flask Web Development.jpg',
             summary=u"""
# This book is not only suitable for beginner web developers to learn to read, but also an excellent reference book for Python programmers to learn advanced web development technology.

* Learn the basic structure of the Flask application and write a sample application;
* Use the necessary components, including templates, databases, web forms, and email support;
* Build large, scalable applications with packages and modules;
* Implement user authentication, roles and profiles;
* Reuse templates, paginate lists, and use rich text in blog sites;
* Implement available functionality on smartphones, tablets and other third-party clients using Flask-based RESTful APIs;
* Learn to run unit tests and improve performance;
* Deploy web applications to production servers.。
""")
book2 = Book(title=u"STL Source code analysis", subtitle=u"Kenting Jieniu is more than enough", author=u"Hou Jie", isbn='9787560926995',
             tags_string=u"Computer, programming,C++", image='STL Source code analysis.png',
             summary=u"""
* Those who learn programming know that reading and parsing famous code is a shortcut to improve levels. Before the source code, there is no secret. The masters' meticulous thinking, experience, technical ideas, and unique styles are all in the original source code.
* The source code presented in this book allows the reader to see the implementation of the vector, the implementation of the list, the implementation of the heap, the implementation of the deque, the implementation of the Red Black tree, the implementation of the hash table, the implementation of the set/map; Implementation of algorithms (sorting, finding, arranging, data movement and replication techniques); even seeing the underlying memory pool and the implementation of higher-order abstract traits mechanisms。""")
book3 = Book(title=u"Compilation principle (2nd edition of the original book）", subtitle=u"原理、技术与工具",
             author="Alfred V. Aho / Monica S.Lam / Ravi Sethi / Jeffrey D. Ullman ", isbn="9787111251217",
             tags_string=u"Computer, principle of compilation", image='Compilation principle (2nd edition of the original book.jpg',
             summary=u"""* This book provides a comprehensive and in-depth discussion of important topics in compiler design, including lexical analysis, grammar analysis, grammar guidance definition and grammar guidance translation, runtime environment, object code generation, code optimization techniques, parallelism detection, and interprocess Analyze the technology and give a number of examples in the relevant chapters. Compared with the previous version, this book has been comprehensively revised to cover the latest developments in compiler development. A large number of systems and references are available in each chapter.
* This book is a classic textbook for compiling principle courses. It is rich in content and is suitable as a textbook for compiling principle courses for undergraduates and postgraduates of computer and related majors in colleges and universities. It is also an excellent reference for the majority of technicians.
""")
book4 = Book(title=u"Deep understanding of computer systems", author="Randal E.Bryant / David O'Hallaron", isbn="9787111321330",
             tags_string=u"Computer, computer system", image='Deep understanding of computer systems.jpg',
             summary=u"""* This book elaborates on the essential concepts of computer systems from the programmer's perspective and shows how these concepts can actually affect the correctness, performance, and usability of the application. The book consists of 12 chapters, including the presentation and processing of information, machine-level representation of the program, processor architecture, optimizer performance, memory hierarchy, links, exception control flow, virtual memory, system-level I/O, network programming. , concurrent programming, etc. The book provides a large number of examples and exercises, and gives partial answers to help readers deepen their understanding of the concepts and knowledge described in the text.
* The biggest advantage of this book is to describe the implementation details of the computer system for the programmer, to help them construct a hierarchical computer system in the brain, from the representation of the lowest-level data in memory to the composition of pipeline instructions, to virtual memory, Go to the build system, to the dynamic load library, to the final user state application. By understanding how the program is mapped to the system and how the program is executed, the reader is better able to understand why the program behaves like this and how inefficiencies are caused.
* This book is suitable for programmers who want to write faster and more reliable programs, and is also suitable as a textbook for undergraduates and postgraduates in computer and related majors in colleges and universities.。""")
book5 = Book(title=u"C# in the shell", subtitle=u"C#5.0 authoritative guide", author=u"Joseph Albahari / Ben Albahari",
             isbn="9787517010845", tags_string=u"Computer, programming, C#", image='C# in the shell.jpg',
             summary=u"""* "C# - c#5.0 authoritative guide in the shell" is an authoritative technical guide for c#5.0, and the first Chinese version of c#5.0 learning materials. Through the contents of Chapter 26, this book systematically, comprehensively and meticulously explains the commands, syntax and usage of c#5.0 from basic knowledge to various advanced features. The book's explanations are simple and straightforward. At the same time, each knowledge point is designed with appropriate, simple and easy-to-understand learning cases, which can help the reader to accurately understand the meaning of the knowledge points and quickly apply what they have learned. Compared with the previous version of c#4.0, this book also adds rich content related to advanced features such as concurrent, asynchronous, dynamic programming, code refinement, security, and com interaction.
* "C# in the shell - c#5.0 authoritative guide" also integrates the author's many years of research and practical experience in software development and c#, very suitable as a self-study tutorial for c# technology, also a book A must-have reference book for middle and senior c# technicians.""")
book6 = Book(title=u"Introduction to Algorithms (2nd Edition of the original book)",
             author="Thomas H.Cormen / Charles E.Leiserson / Ronald L.Rivest / Clifford Stein",
             isbn="9787111187776", tags_string=u"Computer, algorithm", image='http://img3.doubanio.com/lpic/s1959967.jpg',
             summary=u"This book is a comprehensive introduction to computer algorithms. The analysis of each algorithm is both easy to understand and interesting, and maintains mathematical rigor. This book is designed to be comprehensive and suitable for a variety of purposes. Covered by: the role of algorithms in computing, probabilistic analysis and the introduction of random algorithms. The book specifically discusses linear programming, introduces two applications of dynamic programming, an approximation algorithm for randomization and linear programming techniques, as well as a classification method for recursive solving, fast sorting, and a desired linear time-sequence statistical algorithm. And a discussion of greedy algorithm elements. This book also introduces the proof of the correctness of the strongly connected subgraph algorithm, the proof of the NP completeness of the Hamiltonian loop and the subset summation problem. The book provides more than 900 practice and thinking questions and more detailed case studies.")
logs = [Log(user1, book2), Log(user1, book3), Log(user1, book4), Log(user1, book6),
        Log(user2, book1), Log(user2, book3), Log(user2, book5),
        Log(user3, book2), Log(user3, book5)]

db.session.add_all([admin, user1, user2, user3, user4, book1, book2, book3, book4, book5, book6] + logs)
db.session.commit()

app_ctx.pop()
