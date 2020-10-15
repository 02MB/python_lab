favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ryby',
    'phil': 'python',
}
print("Sarah's favorite language is " +
     favorite_languages['sarah'].title() +
      '.')


for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + '.')

for name in favorite_languages.keys():
    print(name.title())

print("\n\n\n\n\n\n")

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
        ", I see your favorite language is " +
        favorite_languages[name].title() + "!")


name_01 = 'erin'
if name_01 not in favorite_languages.keys():
    print(name_01.title() + ", please take our poll!")


for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

print("The folliwing languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())


