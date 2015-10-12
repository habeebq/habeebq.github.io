Title: Setting up Pelican
Date: 2015-10-12
Category: Pelican
Authors: habeebq

I used to blog (when I could!) on Wordpress. Wordpress is great and throws in a huge amount of functionality for free, and also has a huge amount of support.
However, blogging on wordpress.com was a bit limited as I could not (understandably) use any plugins and themes. Also, wordpress was a bit of overkill and also written in PHP which isnt something I am familiar with.
So in order to go deeper, I saw a couple of blogs I liked which had a clean and minimal interface and were generated in Jekyll. So started my journey...

Jekyll looked great, it had a load of themes, well supported and good traction. So I installed it, however, the installation wasnt as smooth as I had hoped it to be, partially due to my overzealous bypassing of most of the documentation. Also I had issues in installing ruby, once I got ruby I needed to install bundler, and I realized I need to update them all in different ways. I was unfamililar with ruby and I wondered if there is something similar available for Python, and hence I found *pelican*.

While Pelican seemed to be less mature than Jekyll, and has less themes, it seemed much more bare, and I felt I could customize and hack it a bit more. There is also Nikola which looks amazing too, but it seemed it requires a bit more support, however it had a similar structure to Jekyll so it must be a good framework too.

[http://blog.getpelican.com/]
[https://getnikola.com/]
[https://jekyllrb.com/]

Never having done web front end it was a bit of a curve for me (and still is) to figure out, but things like jinja, css, bootstrap werent too bad, but I've had to figure things out.

Installing Pelican was easy and editing the pelicanconf.py to set things up was pretty smooth. What I needed to figure out was how to get both the blog on version control and the blog on github static pages at the same time in a single commit. I eventually settled on a structure where I generate the blog static files in a lower directory (habeebq.github.io) and save the blog content, templates and script in a directory called blog within that. This allows me to update the site in a single commit.

Settling on a theme was tough, and I am still not sure. I got Flex working first (adblock was blocking out the font-awesome icons), but then i moved to pelican-bootstrap3. I modified it a bit, to add wells, and to fix markdown tables by enabling the plugin bootstrapify [https://github.com/ingwinlu/pelican-bootstrapify]. There is a huge list of themes here [https://github.com/getpelican/pelican-themes]

Besides I am coming to grips with markdown, I hope to be able to comment all my code in markdown and generate a readable beautified document from it.

I also had to figure out that to get syntax highlighting to work, the code block needs to be indented atleast once.

Now that I type this, it seems I havent done much, but im sure it took my a bit of effort to get my flow running, but i think im almost there. Just need to import my existing blog in here and see how it goes.

As an example here is my current pelicanconf.py

=====
[first link](http://www.google.com)
Reference links [second link][id]

[id]: http://www.google.com

Quotes
======
This guy said:
> Hello to you all

Tables
======
Header  | Header2
------- | ------
Content1| Content2




Is this `monospaced` looking nice?


random block of text

    #!python
	print("This is python")

	:::python
	print("This is also python")

