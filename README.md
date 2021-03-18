# Personal Site 🐍

Welcome to the repo which holds me personal site. This is my little slice of the web, there are others like it but this one is mine.

This is a simple blog built in [Flask](https://flask.palletsprojects.com/en/1.1.x/), using [Contentful](https://www.contentful.com/) to populate my blog posts and [TailWindCSS](https://tailwindcss.com/) and their [typography plugin](https://github.com/tailwindlabs/tailwindcss-typography) for the styling. The site is simple but does the job without being flashy.

### The use of TailWind CSS

When building in a JavaScript environment, adding TailWind and having the abilty to configure it to your liking is pretty straight. However with this Flask project I used TailWind's CDN to get the styling done, I am sure there is a way this can be done just like you can in NPM but I was going for simplicity.

To add TailWind and their typography plugin via CDN just add this to the head of your page:

```html
<link rel="stylesheet" href="https://unpkg.com/tailwindcss@^1.5/dist/base.min.css" />
<link rel="stylesheet" href="https://unpkg.com/tailwindcss@^1.5/dist/components.min.css" />
<link rel="stylesheet" href="https://unpkg.com/@tailwindcss/typography@0.2.x/dist/typography.min.css"/>
<link rel="stylesheet" href="https://unpkg.com/tailwindcss@^1.5/dist/utilities.min.css" />
```

You're able to override the CSS styles, but it's a pain in the ass, especially for the typography plugin IMO at least.