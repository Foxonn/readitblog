from blog.models import Post, Category
from readittags.models import Tag
from django.contrib.auth.models import User
from faker import Faker
import random
import os
from django.conf import settings

user = User.objects.get(username='admin')
fake = Faker()


def generate_text(paragraph=5):
    test = []

    p = []

    for _ in range(paragraph):
        p.append(''.join(fake.paragraphs(nb=paragraph)))

    return ''.join(p)


def random_images():
    images = os.scandir(os.path.join(settings.MEDIA_ROOT, 'fake-images'))
    paths = []

    for img in images:
        paths.append(os.path.join('fake-images', img.name))

    rnd = random.randrange(0, len(paths))

    return paths[rnd]


def generate_category(cat_parent=None):
    title = fake.word()

    if Category.objects.filter(title=title).first():
        return Category.objects.get(title=title)

    category = Category(title=title, author=user)

    if cat_parent:
        category.parent = Category.objects.get(id=cat_parent)

    category.save()

    return category


def generate_post(category):
    post = Post(
        author=user,
        category=category,
        title=fake.name(),
        description=generate_text(),
        short_description=generate_text(1),
        image=random_images())

    post.save()

    for _ in range(random.randrange(2, 7)):
        post.tags.add(generate_tag())

    post.save()

    return post


def generate_tag():
    words = ('Christy Turner',
             'Cody Koch',
             'Colin Curry',
             'Colin Johnson',
             'Craig Patrick',
             'Crystal Terry',
             'Cynthia Porter',
             'Daniel Martinez',
             'David Walton',
             'Deborah Martinez',
             'Debra Parker',
             'Debra Robinson',
             'Denise Phillips',
             'Denise Robinson',
             'Dr. Anna Mckenzie',
             'Eddie Bryant',
             'Elizabeth Ware',
             'Eric Allen',
             'Eric Braun',
             'Erik Brown',
             'Erin Burton',
             'Erin Collier',
             'Frank Vargas',
             'Gerald Garcia',
             'Haley Cook',
             'Heather Mcclure',
             'Isaac Day Jr.',
             'Isaac Smith',
             'James Ross',
             'Jason Smith',
             'Jason Walker',
             'Jay Brown',
             'Jeff Harrison',
             'Jennifer Collins',
             'Jennifer Lawson',
             'Jennifer Tucker',
             'Jesse Baker',
             'Jessica Jones',
             'Jill Hernandez',
             'Jillian Houston',
             'Joel Burgess',
             'Jonathan House',
             'Joshua Kennedy',
             'Joshua Valdez',
             'Justin Hernandez',
             'Kara Alvarez DVM',
             'Kathleen Bradshaw',
             'Kathryn King',
             'Kimberly Taylor',
             'Kristi Ochoa',
             'Kristy Johnson',
             'Lacey Powell',
             'Latasha Hernandez',
             'Leslie Peters',
             'Lindsay Mathis',
             'Lisa White',
             'Lori Hammond',
             'Lori Jones',
             'Luke Perry',
             'Lynn Lopez',
             'Madison Green',
             'Marcus Bauer',
             'Maria Estrada',
             'Mark Dixon',
             'Mark Smith',
             'Mary Holt',
             'Mary Lindsey',
             'Mathew Nguyen',
             'Megan French MD',
             'Michael Anderson',
             'Michael Ball',
             'Michael Frey',
             'Michael Scott',
             'Miguel Baldwin',
             'Mike Hughes',
             'Ms. Claudia Cohen',
             'Natalie Villanueva',
             'Nicholas Garrett',
             'Nicholas Wilcox',
             'Pamela Holmes',
             'Patricia Jones',
             'Paula King',
             'Phillip Brown',
             'Rebecca Wallace',
             'Reginald Cruz',
             'Richard Fields',
             'Robert Ramsey',
             'Robert Williams',
             'Roger Ewing',
             'Samantha Case',
             'Sandy White',
             'Scott Ellis',
             'Scott Montgomery',
             'Sharon Cowan',
             'Shawn Wallace',
             'Stephanie Garcia',
             'Steve Rodriguez',
             'Steven Davis',
             'Steven Perez Jr.',
             'Susan Sanchez',
             'Suzanne Mckinney',
             'Thomas Hammond',
             'Thomas Stewart',
             'Tiffany Barrett',
             'Todd Nixon',
             'Travis Chang',
             'Veronica Moore',
             'William Barker',
             'William Bowen',
             'William Hall',
             'William Martinez',
             'Willie Singh',
             'Zachary Simmons',
             'Zachary Wilson',)

    name = words[random.randint(0, len(words)-1)]

    if Tag.objects.filter(name=name).first():
        return Tag.objects.get(name=name)

    tag = Tag(name=name)
    tag.save()

    return tag


def generate(cat_parent=None):
    category = generate_category(cat_parent)

    for i in range(0, 35):
        generate_post(category)
