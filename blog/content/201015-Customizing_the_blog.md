Title: Customizing the blog
Date: 2015-10-12
Category: Pelican
Authors: habeebq

So I'm no front-end developer. In the past I've tried to understand CSS, but it always felt alien to me. However, hearing and reading about it again and again, possibly rubbed it on to me a little bit. Without CSS we cannot alter the looks of the blog very easily, but using an overriding `custom.css` file, we can override some of the default values and make it more personalized.

I started off with the `pelican-bootstrap3` theme by [DandyDev](https://github.com/DandyDev/pelican-bootstrap3). This guy has put in a lot of effort to port the theme properly to `Pelican` with some extensions. Its a great theme and offers a lot out of the box, but I really wanted to make it look different. The theme also comes with a lot of pre-minified CSS (just CSS compacted for transport) from Thomas Park's [Bootswatch](http://bootswatch.com/). This contained a lot of different and interesting styles for bootstrap.

Lets start by understanding what bootstrap is. Bootstrap is a front-end framework originating from Twitter, that basically has a library of component customisations. The HTML actually defines these components, and assigns each object a class. The bootstrap css, when loaded then styles all of these components. This framework contains a large number of component customisations like grids and tables etc. The main aim, is to make the website **responsive**. This means it loads and scales properly on mobile, tablets and desktops etc. If you see a bootstrap based website, it will look good on any screen size, and will act a bit differently on them, for e.g. the menu and navbar acts differently on mobile vs desktop.

[Bootswatch](http://bootswatch.com/) hosts some nice looking free themes for bootstrap. These mainly change the color schemes etc. Also, fortunately, the `pelican-bootstrap3` comes with these themes already built-in! You do not need to add them yourself.


So lets start off by cloning the bootstrap theme to get a local copy bootstrap theme in Pelican, we can clone the. There are instructions on the [repo](https://github.com/DandyDev/pelican-bootstrap3) github too:

	:::bash
	git clone https://github.com/DandyDev/pelican-bootstrap3.git

And then in your `pelicanconf.py` point to this theme, and also point to any bootstrap theme you like from bootswatch (or you can see all the css options in `pelican-bootstrap3/static/css/bootstrap.*.min.css`)

	:::python
	THEME = '/home/habeeb/workspace/habeebq.github.io/blog/pelican-bootstrap3'
	BOOTSTRAP_THEME = 'readable'
	PYGMENTS_STYLE  = 'monokai'

Ok, so now it looks like a normal bootstrap theme with a navbar and sidebar etc.

Lets start with easy stuff.

I turned the sidebar off and removed categories from the Navbar:

	:::python
    #Navbar
    DISPLAY_CATEGORIES_ON_MENU = False
    #SIDEBAR
    HIDE_SIDEBAR = True

Added some more information to the Article header (the section underneath the article title):

	:::python
    # Article Header
	SHOW_ARTICLE_AUTHOR = True
	SHOW_ARTICLE_CATEGORY = True
	SHOW_DATE_MODIFIED = True

Since the tables werent showing properly I had to install a bootstrap plugin called [pelican-bootstrapify](https://github.com/ingwinlu/pelican-bootstrapify), that cleans up some of bootstraps code. It seems to replace the tags in the table, I am not yet 100% sure what its flow is. 

	:::python
    # Fixing the tables formatting
	PLUGIN_PATHS = ['/home/habeeb/workspace/pelican_plugins/pelican-bootstrapify']
	PLUGINS = ['bootstrapify']

So that was most of the seemingly easy part, however it wasnt so easy when I was trying to figure it out on google and stackoverflow.

Now, how to make changes to the font, colors, navbar, icons, linkcolor and jinja template modifications.

#### Customizing the fonts
Lets start with the fonts, where we used google fonts to make it easier for us. Now the font needs to be defined in the jinja template for base.html. This is in pelican-bootstrapify3/templates/base.html
In the head section of the template we define the following. We have created a new variable called GOOGLEFONT in `pelicanconf.py`

	:::html
    {% if GOOGLEFONT %}
	<link href="{{ GOOGLEFONT }}" rel="stylesheet" type="text/css">
    {% endif %}

Then in the `pelicanconf.py` we define the value of GOOGLEFONT as just the location of it. You can find this location on the Google Fonts website. The bootstrap theme we use also supports an overriding custom.css if it is defined, so we also define that here.

	:::python
    # Bootstrap extra css
	CUSTOM_CSS = 'theme/css/custom.css'
	GOOGLEFONT = 'https://fonts.googleapis.com/css?family=Source+Sans+Pro'

Then create a new file in pelican-bootstrap3/static/css/custom.css or wherever you feel like creating it, but make sure the path mentioned above is correct.

Ok, so we have acheived the inclusion of the font in the html header now, but we havent applied the font anywhere. We will now use the `custom.css` file to override bootstrap's defaults. You can apply the font to any tag, in our case, we applied it to the whole body of the html.

	:::css
	body {
		font-family: "Source Sans Pro","Helvetica Neue","Open Sans",Helvetica,Arial,sans-serif;
		font-size: 18px;
		line-height: 1.728571;
	}

So we have changed the font to Source Sans Pro, with a couple of fallbacks. We also increased the font size and increase the line-height effectively the distance between lines.

#### Customizing the Navbar style
Next I wanted to customize the navbar i.e. the menu bar at the top of the page. Changing the height for that was easy (again in `custom.css`):

	:::css
	.navbar-brand,
	.navbar-nav li a {
		line-height: 70px;
		height: 70px;
		padding-top: 0;
	}

Now, changing the colors of the Navbar was much harder, and I had to use an online tool to generate the CSS for that. See this [link](http://bootstrap3-menu.codedorigin.com/#sthash.RdlMZNJ4.mNUqqyEa.dpbs) and paste the generated css in your `custom.css` again.


#### Font Awesome Icons in the Navbar
Adding font-awesome icons to the Navbar requires modification of the jinja template, again we go back to our `base.html` file. 

We modify the section where MENUITEMS are being iterated over. Add the font awesome icon here (this is possibly not the best way to add the icon in terms of styling/spanning, I need to improve this):

	:::python
	{% for (title, link, icon) in MENUITEMS %}
		<li><a href="{{ link }}"> <i class="fa fa-{{ icon }}"></i>  {{ title }}</a></li>
	{% endfor %}

As you can see this requires an extra icon to be described in the navbar menu item section in the `pelicanconf.py`:

	:::python
	MENUITEMS = (('projects', '/projects.html', 'code-fork'),
             ('whoami', '/about.html', 'user'))


#### Link colors
This next part about changing the link colors is a bit ...hmmm...not the best solution.
The links generated by Pelican seem to all be tagged as 'a' but with no other class name. So the only way to change the link color is to change ALL the link colors sadly. 

Changing the link colors

So I did something like this in my `custom.css`

	:::css
	/* Code tags to be made purple!*/
	a {
		color: #523AB0;
	}

Well, this also changed my header links etc, which I had to override once again to set them back to black:

	:::css
	.page-header {
		color: #000000;
	}

So well, changing the link color might generate too much work. I havent found a way to add a class into it so i can customize it separately.

#### Customizing the page width
Its possible to also control how wide the page body would be. I used the following in my `custom.css`:

	:::css
	@media (min-width: 1000px) {
		.container{
			max-width: 850px;
		}
	}


To be honest I really pulled this value out as my monitor is only 1600x1200 and of that my Taskbar is on the left so causing the browser to get less pixels. I hope it doesnt really matter in the big picture!

So well, there it is, most of my customizations to the bootstrap theme for now. 


