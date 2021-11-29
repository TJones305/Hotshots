# Hotshots

####  A link to the live site is here: [Hotshots](https://inspirasong.herokuapp.com/) 

 **This is a e-commerce type website enabling people to shop online for lawn bowls equipment.** 
 **Users are able to add, edit and update their basket and pay for products**

## User Experience (UX) User stories

### As a user I want to ...
- Be able to navigate the site easily

- Be able to search for items on the site 

- Be able to control and amend products I choose

- Be able to view past orders 

- Be able to register an account

- Be able to read extra content that may help inform my purchasing

- Be able to express my views about a product whether positive or negative to inform other users.


## Design 

### **Colour Scheme** 
The colour scheme for this site was developed with assitancefrom the following site [coolors](https://coolors.co/).
Starting off with Crimson (#D7263D) other complementary colours were suggested using the Cooloers generator, which aided the developer to settle on the following colours completing the scheme Misty Rose(#FFE3DC), Baby Pink(#DBB4AD), Dark Sienna(3B0D11), Black Coffee(#3A2D32) and Dark Liver(#4C4045). The most prodominent throughout the site colours are Crimson, Dark Sienna and Baby Pink.

### **Typography** 
Two font styles were used on the site, courtesy of Google Fonts, the most predominant style was Pontano Sans with the fallback of sans-serif. The developer felt that this font style gave a clean and modern to the site. The Navbar brand has another style Cinzel Deorative with the fallback of cursive. This font was chosen as it appeals to the eye as a standout font, as well as having a stylish, modern look.

### **Imagery** 
As a Bowls e-commerce store the developer felt it was important for there to be a consistent reminder of that throughout the site so starting from the landing page the user is welcomed by the image of a bowls green with some bowls by a jack. This image remains in the background and can been seen it parts through the site. 

### **Wireframes** 

1. Desktop

![Wireframe Desktop](/workspace/Hotshots/media/README_images/wireframe-hotshots-desktop.pdf "Wireframe Desktop")

2. Tablet

![Wireframe Tablet](/workspace/Hotshots/media/README_images/wireframe-hotshots-tablet.pdf "Wireframe Tablet")

3. Mobile

![Wireframe Mobile](/workspace/Hotshots/media/README_images/wireframe-hotshots-mobile.pdf "Wireframe Mobile")

### **Features**
- Responsive on most devices sizes
- Interactive elements (Burger menu (mobile devices only), sidenav, dropdown boxes on post creation, date pickers, collapsible on user profile, modal used to confirm post deletion, registarion and login)

> ## Technologies Used 

### **Languages Used** 
HTML5 
CSS3
JavaScript3
Python3

### **Frameworks, Libraries & Programs Used** 

- Materialize 1.0: Materialize was used to assist with the responsiveness and styling of the website. Specific features include - navbars, burger menu, date picker, modal, collapsible. 
 
- Google Fonts: Google fonts was used to import the two fonts on the site into the style.css file. 

- Font Awesome: Font Awesome was used on buttons to add icons for aesthetic and UX purposes. 

- jQuery: jQuery came with Materialize to make the navbar responsive, along with the other features taken from Materialize. 
 
- Git: Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub. 

- GitHub: GitHub is used to store the projects code after being pushed from Git. 

- Balsamiq: Balsamiq was used to produce wireframes during the design process.

- Heroku: Heroku was use as the platform to deploy the app.

- Django: Django was used to store the colections of the app.

-Jinja: Jinja templating was used extensively throughout the site.

> ## Testing 
The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

### **W3C Markup Validator**

![Markup Validator Report](/README_images/markup-validator.jpg "Markup Validator")
    The Markup Validator highlighted 2 errors. 1 related to href attribute on h4, this was to apply Jinja on the brand logo so when 
    clicked it took the user to the home page, however the developer has now removed this href. the other error relates to a div being a child of a ul.
    The div was placed as such to enable the hero image to load onto the side nav, without it the sidebar was solid black. The developer has decided to
    remove the image, despite it adding a professional touch. 

### **W3C CSS Validator**  

![CSS Validator Report](/README_images/css-validator.jpg "CSS Validator")
	The result of the CSS validator highlighted 3 errors. One error is part of Materialize's CDN. The other Two relate to the rainbow 
    colour scheme created for the main title. The developer feels that this is a justified error to create a wow effect for the user. 

### **Lighthouse** 
![Lighthouse Report Desktop](/README_images/lighthouse-desktop.jpg "Lighthouse Report Desktop")
![Lighthouse Report Mobile](/README_images/lighthouse-mobile.jpg "Lighthouse Report Mobile")


> ## Testing User Stories from User Experience (UX) Section

##  *User Goals*  
- ### Be able to navigate the site easily

- ### Be able to search for items on the site 

- ### Be able to control and amend products I choose

- ### Be able to view past orders 

- ### Be able to register an account

- ### Be able to read extra content that may help inform my purchasing

- ### Be able to express my views about a product whether positive or negative to inform other users.


## **Further Testing** 
- The Website was tested on Google Chrome, Opera, Microsoft Edge and Safari browsers. 
- The website was viewed on a variety of devices such as Desktop, Laptop, iPad Air & iPhoneX. Other devices were tested through the inspect web developer tools.

##  **Known Bugs** 
- 

> ## Deployment 

### **Heroku**  
The project was deployed to Heroku using the following steps...

1. Before you can deploy your app to Heroku, you need to initialize a local Git repository and commit your application code to it.
2. The heroku create CLI command creates a new empty application on Heroku, along with an associated empty Git repository. If you run this command from your app’s root directory, the empty Heroku Git repository is automatically set as a remote for your local repository.
3. You can use the git remote command to confirm that a remote named heroku has been set for your app
4. To deploy your app to Heroku, you typically use the git push command to push the code from your local repository’s master or main branch to your heroku remote
5. Use this same command whenever you want to deploy the latest committed version of your code to Heroku.
6. Note that Heroku only deploys code that you push to master or main. Pushing code to another branch of the heroku remote has no effect. 

### **Forking the GitHub Repository** 
By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the GitHub Repository 
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### **Making a Local Clone**  
1. Log in to GitHub and locate the GitHub Repository Under the repository name, click "Clone or download". 
2. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link. 
3. Open Git Bash Change the current working directory to the location where you want the cloned directory to be made. 
4. Type git clone, and then paste the URL you copied in Step 3. $ git clone https://github.com//TJones305/Hotshots Press Enter. 
5. Your local clone will be created. $ git clone https://github.com//TJones305/Hotshots

> ### *Credits*  

- Bootstrap: Bootstrap Library used throughout the project to make site responsive using the Bootstrap Grid System and implementing the navbar.

- MDN Web Docs: For Pattern Validation code.

- Google Fonts: For use of their brilliant Fonts

- Font Awesome: For use of their icons.

- Content: All content was written by the developer.


> ## Acknowledgements 
- My Mentor Gerry McBride for constructive feedback and continuous support.

- Student support at Code Institute for their helpful advice and guidance throughout the project.