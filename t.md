	Pen testing Stage 2 is the attack stage. All information that you gather during
the pre-attack stage helps you to come up with a thorough attack strategy.
The attack stage involves compromising the target.
You might go after an exploit of vulnerability that you discovered during the
pre-attack stage or even utilize some loopholes like weak security policies or
password policies to try to gain access to the system.
It is important to note that the attacker only needs to worry about one port of
entry or one mechanism to get in, therefore the customer or company needs
to worry about covering all their bases.
Instead of being passive, you need to become active. Once the contract is
finalised and you have permission to engage, first you should try to penetrate
the perimeter by looking at machines that are exposed externally and how
they react.
You then should look at how to enumerate that targets after you have made
your way in. In case you know what the target is, it will be easier to try to
attain the target.
After you attain the target, the next thing you must do is to be able to escalate
your privileges, so you can do more with that particular system. Finally, you
will need to ensure that you can get back into the system by executing,
implanting, and retracting, using rootkits.
Let's get into details on how you would do each one of these items. The
primary ways of testing the perimeter is by going after the firewall itself, and
you are going to do this by sending and crafting some packets to check how
the firewall reacts.
This can be done by looking at how the firewall handles fragmentation,
overlapping fragments, floods of packets.
You can also do this by crafting some packets so you can check the Access
Lists or ACLs of the firewall, such as what's allowed through and what's not.
Technically, what’s permitted and what’s denied. You should also take a look
at how the protocols are filtered by trying to connect to various protocols,
such as SSH, FTP, or even Telnet.
You also must try to measure the thresholds for different denial of service
attacks by trying to send persistent TCP connections and see how the firewall
handles that, or even attempting to stream UDP connections.
By doing this, you will learn what the thresholds are set at the firewall. You
should also try to send some malformed URL-s to see how the IDS respond.
You can also try to see how the web services respond to some requests such
as post request, delete requests, or copy requests. Next, you have to go after
enumerating machines.
The goal of enumerating machines is to find out as much information about
the host as possible. You may have discovered something during the pre-test
environment, but the attack phase gets you active.
But some of those perimeters that you are going to discover could be things
like: what's the machine Id or what's the machine description, and these will
help you identify where the machines are physically located.
You will also need to make an inventory of the network accessibility of these
machines. After you have enumerated the machines, your next step is
acquiring the target.
This is because you know everything on the network or at least a decent
chunk of it. Based on what you have discovered, you can go after those
vulnerabilities.
Some ways that you can gain more information about the target, is by doing
probing assaults. What this means is that you will target those machines you
discovered with different types of assaults to see which ones are vulnerable.
Therefore, you must run vulnerability scans. You also have to acquire the
target by doing something basic like using what known as trusted systems.
This involves trying to access the device's resources through information you
have obtained legitimately through social engineering attacks.
After you have acquired the target, your next step is to escalate the privileges.
Sometimes this escalation is performed by the attacker, so to accomplish this,
you as a pen-tester should try to take advantages of bugs and flaws in the
design of the OS or applications.
Perhaps even misconfigurations on an operating system, or try to elevate
access to an application of a normal user to someone with higher permissions.
Privilege escalation is normally performed by attackers to carry out different
types of activities, such as deleting files, looking at sensitive information or
installing programs that can help them get back in later, such as a Trojan or a
virus.
These technically called backdoors. Some ways that you can escalate your
privileges are include poor security policies or taking advantage of emails or
website coding that's been untested to see if you can gather the information
that could lead to an escalation of privileges.
You can also do it through brute-force attack. Brute-force is more time
consuming, and there are numerous tools out there such as password
crackers, Trojans or even social engineering.
Social engineering is one of the easiest and most preferred ways for attackers
to get in because it's hard to track. After you have escalated the privileges of
an account, the next thing you must do is try to execute, implement, and
retract.
Some systems are vulnerable to a denial of service attacks or buffer
overflows, and some old viruses like rootkits, Trojans, and malware. If you
are able to establish a rootkit or Trojan that can lead to access more
information or more system resources, you must see if you can cover your
tracks by erasing log files or hiding modifications that you have made.
You, as a pen-tester must also need to ensure that you can change system
settings and remain hidden. So you want to see if you are able to be detected
or not.
Once you have done all that, you must ensure that you can get back in via
your backdoor, and see if there is any alerts such as email alerts that
engineers might have been received or been warned.
Chapter 7 Pen Testing @ Stage 3
If you think that the pre-attack steps or the actual attack steps are the most
important, well that’s technically not true. The most critical steps are at the
post-attack stage because you are doing this, from an offensive point of view.
It's the responsibility of the pen-tester to clean up their mess. You are going
to have to ensure that you return the systems to their pre-test state.
You do not just make a mess and leave. Therefore, you should remove any
files that you uploaded, any data that you make modifications to; you'll
ensure that you restore those as well as any settings that you may have
changed.
This is also one of the reasons why it's vital to document each step along the
way. You also must undo any privileges or user settings if you've done any
privilege escalation.
You also must ensure that you restore the network you have made changes to
either within DNS or any IP addresses. In summary, you must recreate the
very same network state as it was before you walked into.
If you've gotten into the registry in any way whatsoever on any system, you
must ensure that you return those to their same settings as well.
Sometimes you might even create different shares and connections, so you
must undo those, and you'll also have to ensure that you document all the logs
that were captured, as well as entries that were modified.
After that, you'll have to analyse the results, and instead of creating problems,
you have to develop solutions. Once you have done all that, you have to
present that documentation to your client, while you must identify critical
system and critical resources that are at risk, and come up with a prioritized
list of what needs to be modified first.
Chapter 8 Penetration Testing Standards
The different ways that you do pen-testing will depend on the methodology
that you decide to use. There are many standards out there. Let’s cover some
of those, so that you can learn which one suit you best.
Let's first begin with the OSSTMM, which stands for Open Source Security
Testing Methodology Manual. This standard set of penetration test is trying
to achieve a high-security matrix.
In summary, this is considered to be the standard for some highest level of
testing. There's another one called OWASP, which stands for Open Web
Application Security Project.
OWASP is an open-source methodology, includes numerous tools that can
help you plenty, and it’s also have a knowledge base, as well as a tool that is
called the ZAPP or the Zed Attack Proxy Project.
ZAPP is a tool that can automatically help you find vulnerabilities in web
applications. ZAPP is designed for web developers, but pen-testers can use
this tool as well.
There's also another framework called ISSAF, which is the Information
System Security Assessment Framework. ISSAF is also an open-source
project on how to conduct a pen-test. ISSAF is supported by a group called
the public information system security group.
Another standard that you should look at is called NIST, which stands for
National Institute of Standards and Technology. When it comes to NIST, you
should know that the federal technology agency works with the industry to
develop and apply technologies, measurements, and standards.
We also have LPT, which stands for EC-Council's License Penetration
Tester. This one is a proprietary methodology, and there is another one from
McAfee, which is called Foundstone and also have ISS, which is done by
IBM.
When it comes to IBM, they do their testing for you. They also had a
signature based product called the Proventia, which is now discontinued. This
was a multifunction security appliance and offered numerous different
services to help secure or test your network environment.
The same thing goes for McAfee and Foundstone too. It’s technically owned
by Intel. With EC-Council's LPT requires the examiner to go through
numerous different steps, similar to the CEH.
You have to go through a course, go through an application process, which
includes a $900 fee, and they will provide access to EC-Council's Aspen
environment.
They do a pen test in a test environment, and they have 30 days to submit
their report to EC-Council. With each of these, whether it's the open-source
or the proprietary versions of these methodologies, all of them are similar one
to another.
Each one of the methods will help you cover all your bases. They all start
with an information-gathering stage, which we've talked about earlier.
It's all about going out and finding as much information as you can about the
target or the company, whether that's from public sources, newspapers,
internet articles, blogs or third-party data sources.
You then have to go through an external pen test, and you are looking for
vulnerabilities that are accessible from the outside. Next, you would look at a
vulnerability analysis so you can find weak points based on software,
operating systems, or machines.
After that, you would do an internal network penetration test to see what type
of information is exposed from the inside. You then go through the firewall
open-testing.
This is your primary line of defense from the outside world, but you would
also do testing from the DMZ. As a side note, DMZ stands for Demilitarized
Zone, sometimes referred to as a perimeter network or screened
subnet.
Next, you must verify that the IDS is doing what it's supposed to do, that
detects intrusions. As a pen-tester, you are going to be looking to see if any
vulnerabilities would allow the attacker to get around the settings of the
alarms that are configured on these systems.
Next, password cracking methods can be used to identify weaknesses
associated with password management. This helps you to ensure that you're
not prone to brute-force attacks, hybrid attacks or dictionary attacks.
These methodologies also ensure that you cover the social engineering pentests. These types of experiments can be done by either using human-based
methods or social engineering with computers, getting someone to open up
an email attachment.
You will also have to cover yourself by looking at web application pen-tests.
You are going to be looking for code-related or back-end vulnerabilities.
Most likely, some more famous tests include SQL pen-test.
SQL injection is still dominant today. It takes advantage of non-validated
input variables that get passed on via SQL commands through the web
application that executes on the back-end database.
Depending on where you put your routers within your network and switches,
they forward data packets from point to point, sometimes inside, and
sometimes outside of your system.
If you take down a router, you end up taking out everybody that's connected
to the internet. When you're pen-testing routers, normally you can do it from
the internet, as well as from the inside.
You will also have to look at the wireless network. Here, you are going to
focus on the availability of outside wireless networks that can be accessed by
employees of the company.
This technically circumvents the company's firewall, because wireless cannot
be restrained, and it goes out everywhere in the air, and we don't see it, and
the signal can be accessed from outside the physical boundaries of the
company's location.
You will also be looking at the strength of the encryption, and the type of
encryption being deployed. You will also continue to cover your bases with
these methodologies by making denial of service test.
See if you can bring down the enterprise network or an e-commerce site by
flooding it with packets or so much traffic that it doesn't know what to do
anymore. When you are making denial of service attack, what you are
looking for is the threshold where the system starts to have a break down.
You should think about how you would handle stolen machines. For
example, once you have locked down all your phones and laptops, you
should also think about what happens when those machines get stolen.
For example, the pen-testing team can try to take mobile equipment and
conduct offline tests to gain access to the information stored in those offline
machines.
For example you should not go after someone's computer in the sales
department, instead try to focus your attack towards somebody that you have
identified as an IT person.
If you can get someone from the IT department or someone in a senior
management, well, those people have more permission or access to more
systems then the rest of the employees.
You also have to look at source code penetration tests. Many companies
today are using applications that are created in-house, and sometimes these
applications aren't even considered as part of the security platform.
As a pen-tester, you're going to look at the source code either manually, or
there are numerous tools that could help you such as Zappit.
In this type of testing, the testing team will try to gain access to the facilities
before, during, and after business hours, but must not do any destructive
things.
For example, you don't break windows, but if you can pick the lock easily, or
able to disassemble the gate, or jump turnstiles, it’s fine with many
companies.
Some companies are a little scared about that type of test being done, so
another thing you should do is to do walkthroughs to provide the company
with an objective perspective of their security controls that are currently in
place, and how they could be bypassed.
Similarly, check if the company have cameras? If so, you want to understand
if they operate with a web interface. What is their viewing angles? For
example you can utilize a drone to fly into an area to look at the top of the
camera to look behind the camera without being detected.
In summary, you are able to look at how much motion is allowed before the
camera kicks in or where is the visibility of the camera. You will also need to
ensure that you look at databases.
This is where you are going to try to directly access data contained in the
database by trying to utilize some password cracking methods. You could
also try to make your standard SQL injection attack, but not databases that
are SQL-based.
You will also have to look at data leakage. Here, you must understand if the
data you discover contains any intellectual property, private, or sensitive data.
This particular pen test should try to help the company to prevent confidential
information from going out into the market or to competitors. Therefore, you
should check who has access to those files?
You should also try to improve awareness amongst employees on the best
practices. This is more targeted, but if the company is using a SAPP platform,
you may implement a pen-test to see if it's been patched correctly.
This is, so you can find out if there are any vulnerabilities that an attacker
could utilize since SAPP has a lot of business-critical information within it.
Another area to take a look at when you pen-testing is the VPN or Virtual
Private Network pen-test.
Most companies allow some of their employees to work remotely either if
they're on the road or working from home. In either case, VPN-s create
trusted connection to the internal network.
It knows that the pen-tester will try to gain access to the VPN either by trying
to compromise a remote endpoint or trying to gain access to the VPN tunnel,
so they can gain access into the network.
Moreover, you should also try to gain access to the VoIP or Voice over IP
network to try to record conversations or make a denial of service so they
cannot communicate.
Another popular feature is the cloud, so when you start using it, security is
based on the shared responsibility of both the provider and the client, and
there are many security risks associated with cloud computing.
Other tests that you should accomplish include virtual devices. Most
companies already using virtualization. Because the host device is fully
patched, doesn't mean that the VM or Virtual Machine is.
What you might find is that the virtual appliance is patched, but the host isn't,
and because the virtual environment is an exact duplication of the physical
environment, it suffers the same security concerns.
If the VM is running software or applications, then it's vulnerable. The
attacker doesn't care if it's virtual or not. It's just another target.
When you do these types of tests, you are looking to see if you are able to get
through an older technology that may be a company has forgotten about.
You must see if there are any old modems still holding their default
passwords too. The modems are identifying themselves via a banner.
Whether it's a Trojan, a virus or ransomware, but for example Trojans
designed to steal sensitive information, delete data, replace operating system
files, maybe even perform a denial of service attack, start watching you with
key loggers, create backdoors, or provide remote access.
Viruses are designed to destroy data, slow systems down, consume resources,
and you also have the issue with ransomware. As a penetration tester, you
want to ensure that you look for any ports that may be suspicious that are
open.
Moreover, you should look for any processes or registry entries, or machine
drivers that are infected, Windows services or fake services, what programs
have network access, how do users or employees handle malware or
ransomware coming through email, and so on and so forth.
Another thing you should consider when you're doing your pen-testing, is
looking at log management. Log files record the who, what, where, when, of
everything on the network, so managing those log files, making sure that
they're put in locations that are properly secured, or monitoring them for any
modifications.
Once is too late, you should also be testing for their file integrity. How are
they handling that? Here, you should make sure that no files are being
tampered with, especially when it comes to operating system files.
That also related to malware, but you should be trying to identify who
modified the data, what are the attributes and how are those recorded and
maintained.
When it comes to mobile devices, well, everyone's having mobile devices
nowadays. Everybody wants to be on mobile, and BYOD or Bring Your Own
Device deployments are becoming very popular, so you have to start
monitoring and checking out people's mobile devices.
Because these portable machines operate with different Operating Systems
and different applications, it introduces new security issues for us all.
Technically, there should be one person monitoring mobile devices at all
times. We talked about VoIP, but we also have telecom and broadband
penetration testing.
It doesn't matter which business in what building you are looking at; you can
gather everybody’s data. One of the most significant ways that people get in
to the system is using malware and ransomware through email, so that you
should be looking at email security too.
Email is the most used communication in the world today. But the main
reason it’s important, is because we're using email to store personal
information and corporate data with attachments.
For example, if you are able to get a hold of the CIO-s or CTO-s account, it
could be a significant impact on the company. Therefore email security
should be looked at from both internally and externally.
Chapter 9 Introduction to Footprinting
When it comes to penetration testing and footprinting the target, the purpose
is to determine what information is available publicly of your target. These
are information that's available on the internet, such as network architecture,
operating systems, applications or users.
This is passive as far as the research is concerned. You as a pen-tester have to
try any possible way that you can to go after either hosts or networks.
It could be either of them, but you have to use any possible way that you can
to gather as much information as possible before you get into the next stage
of the penetration test.
If you find sensitive information on any website or any location that's
publicly available, that information needs to be reported to the organization in
your report.
If you find information that you believe is critical and you think it should not
wait a month or even a week before you submit the full report, you want to
notify your emergency contact immediately.
This stage of the attack should help preventing information leakage, and help
you with social engineering attempts. Let’s look at specifics.
The first thing you can do is get proper authorization, and that's going to be
from whoever is in charge. It may or may not include system administrators.
Many times companies must know how their system admins are performing.
After you go through that process, you must ensure that you define the scope.
Limiting the scope of the pen test is a prerequisite. Going through this stage
helps to set you up the list of items needs to be tested. For example; what are
the IP ranges or subnet ranges of the systems, or what are your limitations.
After you've defined the scope, you should plan and gather information about
that scope using your reconnaissance tools. You have to start with search
engines such as Google, Bing or Yahoo, whichever one you must use to look
at what information is currently being exposed.
You can also check some other specific sites too such as social networking
sites like Facebook, and see if there is a Facebook page or Twitter account for
the company.
Next, you should see who are friends of that company because that's where
you are going to find existing employees and see if you can backtrack from
there.
After you are done looking through the search engines, you have to try to see
if you can “Google hack” them. You can do that by utilizing additional tools
that give you a Graphical User Interface such as SiteDigger or the Google
Hacking Database.
By doing Google hacking, it will allow you to find resources that have been
crawled by the Google search engine that companies may not know are being
listed there such as printers or cameras, which could provide you an insight
of IP addresses that are exposed, or what the machine they have.
Your next step after the Google hack is to go after social networks, such as
Facebook, Twitter or LinkedIn.
People have a tendency at the social networking level to let their guards
down. It's easy not to see what people are talking about, but start-up
conversations with users or the employees could be a great way to gather
information.
You might go and start a chat with an existing employee and say: “Hi, it
looks like you've got an excellent company, and I have been thinking about
joining the IT team. What type of devices do you use in there?”
Your next step is to go and footprint the websites, and you are going to do
that with either BlackWidow or Web Site Copier. With these tool, first you
have to download their website so that you can look at it offline and look at
the code.
You have to remember that everything that's presented to you in a web
interface are files that are downloaded to your system. Therefore why not
download an exact copy of that website so you can take a look at what they're
doing at the back-end, particularly if they're making calls from the front-end
to the back-end.
Next, you can start looking into some email footprinting. You can use some
great tools that'll do that for you such as the “nslookup” command to find out
the DNS names and IP addresses of their servers.
Some of the information that you can get out from emails includes the
encryption that they're using and other services that could be used along with
their email environment.
You can also find out how they are hosting the email servers or what hosting
providers they use. Next, you can do some competitive intelligence.
Competitive intelligence is the way that most businesses are using to find out
about their competitors. Attackers can use the very these same resources to
find out what the people are doing, and it's also an excellent way for
companies to discover what projects their competitors are working currently.
Next, you should do a “whois” reconnaissance, so you can find out who owns
the IP address range or their domain. To accomplish this, you can use tools
such as Domain Dossier or SmartWhois.
Sometimes these tools will also do some necessary enumeration based on
DNS, which is your next step. For DNS reconnaissance, you can use tools
such as Sam Spade or DNSstuff, but you always use the “nslookup”
command too, which is very powerful.
One of the reasons why you should do a DNS reconnaissance is because you
are able to determine key hosts in the network that you can then use to
perform social engineering attacks or you could use during a DNS poisoning
attack.
Your next step is to perform a network reconnaissance. For this purpose, you
should use types of tools, such as “Path Analyzer Pro”, which will shows you
the path that a packet takes, or Network Pinger or VisualRoute tool that
allows you to find out further information about the targeted network.
These will help you to draw a better diagram of what you are dealing with.
You should also try some social engineering attack that includes “shoulder
surfing” to see if you can gather information by watching what people are
doing.
Other social engineering attacks also include dumpster diving or
eavesdropping. These will allow you to gather information, such as the
organization's security products that they're using, operating systems,
software versions, network layout, IP addresses or the names of their servers.
You must ensure that you document everything that you find. This is because
you will have to use this document and all the information that you have
collected to understand and analyse the security posture of your target.
You will be surprised with the information you can conclude from what you
pull off using this method. This is why it's so important to spend as much
time as possible here, so you can create a map of everything else you're about
to do.

