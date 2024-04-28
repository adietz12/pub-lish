#Create mongita database with article information
import json
from mongita import MongitaClientDisk

#This one is for dates
from datetime import datetime
# Function to convert date string to datetime object
def convert_date(date_str):
    # Assuming the date format is 'month/day/year'
    month, day, year = map(int, date_str.split('/'))
    return datetime(year, month, day)


#Put future articles in this array then just index it in the actual db so it doesn't clutter it up
article = ["""
School of Fashion students are collaborating with fitness guru Jaime Brenkus to compete for their t-shirt design to be featured on his show.

Brenkus rose to popularity in the 1990s after he created the program “8-Minute Abs.” Since then, Brenkus has helped millions of people meet their fitness goals.

Over the last two years, Brenkus and associate fashion professor Vince Quevedo have created a program that will help prepare students for the real world.

“I think the biggest thing is knowing that basically putting the students in an arrangement gives them a platform for the students to achieve,” Brenkus said. “We call it a real life experience with a national brand.”

Quevedo’s students each make a t-shirt design suited to Brenkus. Once the competition is over, Brenkus chooses a design to wear on his PBS program. Not only does this allow students a chance to design their own piece of fitness apparel, but also the chance to be featured on a major platform.

With nearly 1,500 students in fashion design and fashion merchandising, the collaboration has many benefits. For fashion students, this opportunity is preparing them for their future even while they are still in school.

With fitness at the forefront of the assignment, Brenkus explained his steps to start a fitness journey.

“I think you have to look at and see what your goals and objectives are, whether it’s to basically lose weight or whether it’s to shape your life. You have to go back to tried and true strategies,” he said.

The collaboration between Kent State students and Brenkus has offered a good experience for both parties.

“Students themselves exemplified the type of curriculum that Kent State has, because they’re very bright and talented,” Brenkus said. “When everybody created shirts for us, I gotta tell you, I could have probably used every single one of them.”
""",
"""
April is Sexual Assault Prevention and Awareness Month (SAAM). Several events are occurring on campus throughout the month, such as a Denim Day fashion show, to shed light on SAAM.

SAAM was nationally recognized for the first time in 2009 by former president Barack Obama. However, the National Sexual Violence Resource Center (NSVRC) first started recognizing SAAM in 2001.

NSVRC aims to share more resources with the public, Halle Nelson, communications specialist with NSVRC, said in an email.

“Sexual harassment, assault, and abuse are a longstanding, pervasive issue in our culture, and it is our goal to remove stigma around that conversation, empower survivors through education, amplify local and state resources for survivors to pursue and reinforce to the public that sexual violence is preventable,” Nelson said.

SAAM allows for a more concentrated effort to bring awareness to sexual assault, a conversation that NSVRC has all year, Nelson said.

“Each April, we encourage allies and fellow sexual violence-combatting organizations across the nation to participate in hosting events, posting on social media and doing any other sort of activity to amplify the issue of sexual violence in their communities,” she said. “Sexual violence-based prevention, education and advocacy is a year-round effort, but we are particularly pleased to see how many people have used SAAM as an opportunity to open up discussion about such an important topic.”

Sexual assault awareness does not have to always be regarded as a depressing or heavy topic, Nelson said in an email.

“It’s a chance to uplift and champion inspiring figures and advocates,” she said. “It’s a time to honor how much progress has been made by advocates, largely women, who fought to have their issues recognized by the public. When you look at it that way, it’s a time of education, hope and perseverance.”

When it comes to college campuses specifically, Rape, Abuse and Incest National Netwrok (RAINN) says, “among undergraduate students, 26.4% of females and 6.8% of males experience rape or sexual assault through physical force, violence or incapacitation.”

Looking more directly at the Kent State campus, the university is required to release a security report annually. Past reports have shown that the university reported 16 instances of rape on campus in 2021. Additionally, the university has reported 12 instances of rape on campus in 2022.

On campus, the Center for Sexual and Relationship Violence Services (SRVSS) is a resource that students can reach out to if they have questions or need support. They also provide educational resources about sexual assault and relationship violence.

SRVSS uses SAAM to make more people aware of the prevalence of sexual assault in society, Julis Payne, program director for SRVSS, said.

“Sexual assault awareness month is an awareness month that sheds light on the issue of power-based personal violence, as far as sexual assault goes,” Payne said. “So it’s an opportunity to put on programs, to market different things, to just raise awareness for individuals to know how big of an issue sexual assault is, not only on college campuses, but in our communities and just in our country in general.”

When talking about sexual assault, there are often misconceptions about the frequency of it occurring, and about who is impacted by these situations.

“I mean, as progressive as we are, there’s still a misconception that it doesn’t happen to guys, or that whatever the situation may be, a guy can get himself out of that,” Payne said. “Another one is the misconception that people are lying when they say that something has happened to them. Realistically, statistically, the same amount of people lie about sexual assault that lie about other crimes.”

SRVSS uses educational efforts to try and remove these misconceptions from people’s minds and change the narrative they may have about sexual assault, Payne said.

One event SRVSS is having on campus is the ‘Denim Day Fashion Show’. It is being put on by Deandra Wright, a senior advertising and communications major and India Gardener, a senior journalism major.

Denim Day takes place on the last Wednesday of April, and it is in recognition of an infamous Italian Supreme Court ruling, in which a rape conviction was overturned because of the clothing the victim was wearing.

The Supreme Court believed that since the victim was wearing tight denim jeans, she would have had to help the perpetrator remove her pants, implying consent.

The story of Denim Day could resonate with many women who have been in similar situations, and the students want to use the fashion show to shed light on it, Gardener said.

“Our job, when it comes to denim day, is to show people that you can be assaulted in any amount of clothes that you are wearing, and any type of clothes that you are wearing,” she said. “Regardless of it being denim or something being tight, it can happen to anyone.”

The event will include a fashion show and presentation about what denim day is, so students can learn more. It will be held Wednesday, April 24, from 6-8 p.m. in the Oscar-Ritchie Theater.

Gardener and Wright hope to bring awareness to the resources available to students through this event.

“Our main goal is to include you in here, get you involved, get you educated and not only realize there are resources on the Kent campus but also there are resources you can point out to your friends,” Gardener said. “A lot of people don’t know the type of support services that SRVSS offer.”

SAAM as a whole, including Denim Day, can help raise awareness for something that people often shy away from talking about, Wright said.

“It’s just a month to honor victims of sexual assault, to have these conversations,” she said. “Because daily people are sexually assaulted, it’s often hidden. These are often conversations we shy away from even today, the justice system has a lot of work to do. So SAAM is really important to cause awareness and bring awareness to these issues, so that we can move forward as a society and begin to fix them.”

Just a few of the other events that SRVSS has put on this month include the “What Were You Wearing” exhibit, the Day of Action and More Than Words.

‘What Were You Wearing’ was an exhibit recreating outfits that both women and men have been sexually assaulted in. The goal was to educate people that sexual assault can occur no matter what a person is wearing, Gardener said. It ran from April 6-14, in the Williamson House and the Center for Visual Arts.

“With our ‘Day of Action’ event, it’s just us getting toiletries and stuff together for underprivileged people,” Gardener said. The drop-off deadline for collecting items was April 12, but the care package making will occur April 30.

The ‘More Than Words’ event was a space for people to come into the Williamson House and create art while meeting with people to share their stories and receive support from the community, Wright said. The event occurred April 16 from 3 to 4:30 p.m.

The rest of the events for the month can be located on the SRVSS website.

One of the best ways to support a friend or family member who comes to you for support regarding sexual assault is to believe them, Payne said.

“If you believe that something happened to that person, you’re going to give them resources,” Payne said. “If you believe them, you’ll get them to somebody who can help them.”

The Williamson House is located at 1175 Risman Dr. It is open Monday through Friday from 8 a.m. to 5 p.m. for anyone who wants to talk or spend time in a safe space.

“There is no shame in reaching out,” Payne said. “There is no shame in using the resources, that is what we are here for. It could be something that happened years ago, that you just need to unwind. If you just need to talk to somebody, you can come to us.”
""",
"""
On the night of a formal dance at their high school, Aiden Zapisek, who identifies as non-binary and gay, entered a stall in the men’s bathroom. Soon after, a group of boys walked in and surrounded the stall door.

With their heart pounding, Zapisek froze as the boys banged on the door while yelling, moaning and throwing things into the stall.

“It was definitely hard to come around after that happened,” Zapisek said. “I’m okay with it now. It sucks that it happened, but screw them.”

Now a freshman digital media production major, Zapisek said they hope to be a voice for non-binary, trans and gender-nonconforming people who don’t feel safe using public restrooms.

When they first heard about House Bill 183, Ohio’s latest bill that would require K-12 and college students to use bathrooms and locker rooms that align with their sex assigned at birth, all they could think about were students who have had similar experiences while trying to use the bathroom.

“As somebody who is non-binary and does use a male restroom, I’m not extremely comfortable with it,” Zapisek said. “I’ve had men bang on doors and be like, ‘Hey, what are you doing in there?’ and just yell and be loud, and it’s very uncomfortable. So, I understand if somebody feels comfortable in one bathroom over the other, or if they identify as female and want to go in a female bathroom, they should be able to do that and vice versa.”

The House Higher Education Committee approved the bill, which would also ban schools from letting students share overnight accommodations with the opposite biological sex, on April 10.

Ohio House Reps. Beth Lear and Adam Bird, who introduced H.B. 183 last May, did not respond to KentWired’s request for comment.

The bill comes amid a nationwide push to restrict transgender people’s access to public restrooms, locker rooms and other facilities. Similar bills have passed in states such as Utah and have been introduced in Idaho, Georgia, Arizona, New Mexico, Iowa and West Virginia.

Zapisek said one of their trans friends, who lives on campus, said there was a debate over whether they were allowed to use the bathroom on their “female-only” floor because they identify as a trans man.

“They ended up being able to use the bathroom, but it was a serious dilemma and situation,” Zapisek said.

For Lauren Vachon, an assistant professor and coordinator of the LGBTQ Studies program, the bathroom debate hits close to home.

Vachon’s trans son, Jeremy, came out in high school and wanted to feel comfortable using the school bathrooms. When Vachon and their son walked into a meeting with the school district to discuss accommodations, they were surprised by the school’s willingness to accommodate.

The school offered him to use a separate restroom, which made him the most comfortable. While Vachon believed it was a better option, they didn’t feel it was truly equal.

“I felt that ‘use this special bathroom’ was not true, equal access, right?” Vachon said. “I agreed that it was probably best for Jeremy, and he also agreed, but my feelings about it were complicated. Really, I had gone into that meeting with school administrators ready to do battle — but I didn’t have to.”

Vachon has been a professor at Kent State since 2016, and they said they’ve heard from many queer and trans students who are concerned for their safety as H.B. 183 advances.

“The kind of policing of bathrooms that this bill will engender will make it dangerous for these students to use public restrooms on campus,” Vachon said.

However, Bird told the Ohio Capital Journal that H.B. 183 will give Ohioans protections in restrooms.

“Me and my Republican colleagues have heard from constituents all across the state,” Bird said. “They may not have been loud. They may not have been vocal. They may not have come with a sign to the Statehouse, but we are here representing the vast majority of Ohioans who want protections.”

Vachon said they don’t believe the bill will solve Ohioans’ problems, and they said Republican members of the Statehouse are engaging in “performative politics.” They said members are catering to conservative organizations, such as the Alliance Defending Freedom and the Heritage Foundation, which they said are the machines behind this type of legislation.

“That produces this alignment where all the Republicans in state houses in Ohio and other states feel compelled to introduce these bills that are sometimes almost identical in their wording because they’ve been written by these national groups,” Vachon said.

One aspect of the bill that Vachon is especially concerned about is its vague enforcement mechanism, which heavily relies on an individual’s biological sex listed on their birth certificate. The bill defines biological sex as “the biological indication of male and female, including sex chromosomes, naturally occurring sex hormones, gonads and nonambiguous internal and external genitalia present at birth, without regard to an individual’s psychological, chosen or subjective experience of gender.”

Vachon said that even if queer and transgender students have had their gender markers on their birth certificate changed, it won’t be enough.

“What’s going to happen to a trans man who has a full beard who’s [going to] have to use the women’s room?” Vachon said. “There’s the other scenario of trans women having to use the men’s room, and that is incredibly unsafe for trans women.”

Research has found that transgender women experience assault about four times higher than cisgender women. The human rights organization GLSEN found in a 2021 Ohio report on the experiences of LGBTQ+ middle and high school students that 42% of trans and non-binary students were stopped from using the bathroom that aligned with their gender, and 36% couldn’t use the locker room aligning with their gender.

If H.B. 183 passes, Vachon said non-binary and trans students should seek out safe bathrooms for themselves, and they said the LGBTQ+ Center maintains a list of where all the universal restrooms are located on campus.

“My advice is for people to seek out safe bathrooms for themselves,” Vachon said. “Kent State is installing quite a few restrooms that will be key if this bill were to become law — the ones that have a single toilet and a sink behind a locked door. Under this bill, those would still be allowed to be considered universal restrooms if they’re like that style.”

Erica Pelz, a faculty member and sophomore sociology student, said the bill is a direct attack on all women. Pelz spoke outside of their role with the university.

“I’m very worried about both trans students and cisgender students who are going to be challenged by people with nefarious intentions who are just trying to go pee,” Pelz said. “‘Prove to me that you should be in the women’s restroom. Prove that you’re really a woman,’ you know?”

As a trans woman, Pelz said LGBTQ+ people and allies should assess their risk before speaking out against H.B. 183 and similar bills.

“If you can tolerate that risk, start calling representatives, start writing letters and be heard,” Pelz said. “When you hear somebody say something that is blatantly untrue about trans folks and bathrooms, correct them and explain why it matters.”
""",
"""

""",]
#Put future articles in here the way it is formatted
print(article)
publish_data = [
    {"pop":"1","author":"Lauren Vaughn", "title":"School of Fashion collaborates with ’90s fitness guru for t-shirt design contest", "text":article[0], "date_created":convert_date("4/28/24"), "date_string":"4/28/24"},
    {"pop":"1","author":"Olivia Montgomery", "title":"Sexual Assault Awareness Month provides support for students and community", "text":article[1], "date_created":convert_date("3/28/24"), "date_string":"3/28/24"}
    {"pop":"1","author":"Aden Graves", "title":"Inside House Bill 183: Ohio’s latest bathroom bill", "text":article[2], "date_created":convert_date("3/28/24"), "date_string":"3/28/24"}
]

#Create a mongita client connection
client = MongitaClientDisk()

#Create article database
articles_db = client.articles_db

#Create articles collections
article_collection = articles_db.article_collection

#empty the collection
article_collection.delete_many({})

#Put the quotes in the database
article_collection.insert_many(publish_data)

#Check if articles are there
print(article_collection.count_documents({}))
