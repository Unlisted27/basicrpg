If you understand everything that's going on here, you probably don't need to read this.

**VVV FOR THE NOOBS VVV**
_If you are inexperienced, and all of these files in what you thought should be a simple python script looks really scary, read this._
Basically, I hope you have used libraries/modules, y'know, when you do pip install. Basically, this is the same thing but everything is local. Why not just store all myy functions and objects in one script? I could, but it's unorganised and can make the final script difficult to read. Instead, we have a utils folder which contains a bunch of things that you will see are imported at the top of other scripts. This also means that if you are having an error with one of the custom functions that have been imported, you can simply look at where it's coming from (ex: components.character.attack() would be located under /utils/components), go there, and see the behind the scenes for a better understanding of your issue.