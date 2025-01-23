# The Witches Society

[Live site](https://witches-society-e36df8ff45ed.herokuapp.com/)

![amiresponsive screenshot](documentation/amiresponsive.png)

The Witches Society is an online submission blog page where users can submit their own spells to a collaborative Grimoire. The site provides a fun community space where like minded individuals can come together and share their spell knowledge. All users are free to browse the blog. Users may create a user profile account if they wish to contribute their own spells to the blog.

## User Experience (UX)

After researching into similar existing witch themed sites I decided to opt for a simple, feminine, monochomatic colour palette as I found most sites to be overwhelmingly dark in theme.

![colour palette](documentation/color-palette.png)

## Fonts

- [Irish Grover](https://fonts.google.com/specimen/Irish+Grover/tester?categoryFilters=Appearance:%2FTheme%2FWacky) was used for the site Logo.
- [Rubik](https://fonts.google.com/specimen/Rubik) was used for the site's main content.

## User stories

User stories can be found [here](https://github.com/users/Jahooli4/projects/4/views/1) via my gitHub project.

## Structure Plane

### Home page:
- Site logo
- Navigation bar with links (Left side)
- Navigation bar with login/logout and profile/register links (right side)
- Hero image carousel featuring moon landscape images
- Welcome message with brief site description
- Footer section with links to social media

### About page:
- Navigation bar with logo/links
- Information about the purpose and function of the site hidden behind visually appealing interactive flip cards
- Footer

### Blog page: 
- Navigation bar with logo/links
- List of spell submission blog posts in chronological order, most recent first
- Posts are just previews, showing feature image, title, author and date posted
- Pagination: allows users to navigate between pages of posts
- Footer

### Post detail page
- Full blog post including content is displayed
- If the current logged in user is also the post author then the edit/delete option buttons will be visible

### Register page
- Sign up form with required fields for users to create an account
- Default profile image is used if user does not upload their own

### Profile page
- Shows user's account information
- Update button that reveals a profile update form should users wish to edit their information

### Submit a spell page
- Only accessible to logged in users
- Form allows users to submit spell blog posts

## Existing Features
### Site pages:
#### Home page
The landing page for the Witches Society is simple and clean with intuitive navigation. A hero slideshow offers a more engaging option than a single image.

![Home page](documentation/homepage.png)

### Footer section
The footer section contains all relevant site and social media links. Account links are displayed for logged in users.

![Home page2](documentation/footer.png)

### About page
The about page contains information about the site owners, the site's purpose, and how to use it. The information text is neatly concealed behind flip cards with a tarot card front to keep the visual design on brand.

![About page](documentation/aboutpage.png)
![About page](documentation/aboutpage2.png)

### Spell blog page
The blog page is organised with each blog post displayed featuring the post image, title, author and date. The posts are displayed in orde rof date posted, with the most recent at the top.

![Blog page](documentation/blogpage.png)

### Pagination
Both blog and user post pages are paginated by 6, when the post count eceeds this numbered buttons are displayed at the bottom of the page to make navigation user friendly.

![Pagination](documentation/pagination.png)

### Post detail
The post detail displays the full blog post content and photo, including a small thumbnail of the author's profile picture.

![Post detail](documentation/postdetail.png)

### Post edit
The edit/delete buttons are only visible to the logged in post author.

![Post edit](documentation/postedit.png)

### Post Delete
Double checks the user is sure they want to delete their post to avoid accidental one click deletes.

![Post edit](documentation/postdelete.png)

### User posts page
If a user clicks on an author's username on any page then they will be taken to a page displaying a list of posts by that author.

![User posts](documentation/userpost.png)

### Spell submition page
The spell submission page features a form that allows users to ubmit their own spell posts to the blog. If users neglect to upload a photo then a default header image is automatically added instead.

![Spell submition form](documentation/spellsubmit.png)

### Register page
Provides a form for users to fill out should they wish to create an account and access logged in user features.

![Register page](documentation/register.png)

### Profile page
The profile page displays the user's information in a clean and organised way. An 'edit profile' button has been provided should users wish to update any of their details. When clicked it reveals the update profile form.

![Profile page](documentation/profile.png)

### Edit profile form
Contains all the relevent fields a user may wish to alter, including their profile picture.

![Edit profile form](documentation/profileedit.png)

### Logout
Alerts users that they have successfully logged out.

![Logout page](documentation/logout.png)

## Future features

### Front end admin panel
- Would allow admin users to access user profiles and investigate any issues they may have.
- Admin users would be able to delete any user's posts, not just the ones they have created.

### Password reset
- A feature to allow users to reset their passwords, users would be sent an email with a link.
- This is a fairly essential feature to prevent users being locked out of their accounts without having to contact admin to resolve the issue.

### 