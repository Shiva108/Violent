# Ports from armitage
50000, 21, 1720, 80, 443, 143, 623, 3306, 110, 5432, 25, 22, 23, 1521, 50013, 161, 2222, 17185, 135, 8080, 4848, 1433, 5560, 512, 513, 514, 445, 5900, 5901, 5902, 5903, 5904, 5905, 5906, 5907, 5908, 5909, 5038, 111, 139, 49, 515, 7787, 2947, 7144, 9080, 8812, 2525, 2207, 3050, 5405, 1723, 1099, 5555, 921, 10001, 123, 3690, 548, 617, 6112, 6667, 3632, 783, 10050, 38292, 12174, 2967, 5168, 3628, 7777, 6101, 10000, 6504, 41523, 41524, 2000, 1900, 10202, 6503, 6070, 6502, 6050, 2103, 41025, 44334, 2100, 5554, 12203, 26000, 4000, 1000, 8014, 5250, 34443, 8028, 8008, 7510, 9495, 1581, 8000, 18881, 57772, 9090, 9999, 81, 3000, 8300, 8800, 8090, 389, 10203, 5093, 1533, 13500, 705, 4659, 20031, 16102, 6080, 6660, 11000, 19810, 3057, 6905, 1100, 10616, 10628, 5051, 1582, 65535, 105, 22222, 30000, 113, 1755, 407, 1434, 2049, 689, 3128, 20222, 20034, 7580, 7579, 38080, 12401, 910, 912, 11234, 46823, 5061, 5060, 2380, 69, 5800, 62514, 42, 5631, 902, 5985, 5986, 6000, 6001, 6002, 6003, 6004, 6005, 6006, 6007, 47001, 523, 3500, 6379, 8834

#
OSCP Script needs

1
)
Recon scripts: Automated recon of a network. This will give us a generic idea of what kind of machines are on the network and the various OS

's and possible "sweet spots" to start the exploitation process. Only the top 10-20 ports are scanned but we'
re scanning the whole

/
24
range.

2
)
Mapping scripts: Mapping is where I aggregate the data gathered from the recon scripts and start to make sense of things. This includes relationships between systems and traffic flows. This is a manual step which will be done in Visio manually. I have built a Visio template diagram which I will use for this purpose. Mapping will be a continuous process as I move forward in the lab and the Visio diagram will be updated on an almost daily basis.

3
)
Remote enumeration scripts: These are scripts which will scan a single system remotely, mostly enumerating ports and shares but also the information FROM those ports. This is where the full

1
-65535 ports will be scanned

(
both TCP and UDP

)
and where each port is fingerprinted, SMB shares are enumerated, user IDs, SNMP details, FTP banners, OS versions etc

4
)
Remote Exploits & Privilege Escalation: Here we move from knocking on the door to bashing the door out of its sockets and force entry in to the remote system. This includes remote

"point-and-shoot-instant-system-access"
,
FTP brute-force, HTTP directory brute force, SNMP brute force, active exploits against open services, etc

5
)
Local Enumeration scripts: Once we have entered the machine remotely, we enumerate again, getting as much information from the system as possible. This includes interesting files, bash history, cmd history, environment settings, memory, running services, directory permissions, service permissions, scheduled jobs, weak permissions etc

6
)
Local Exploits & Privilege escalation: We might have a low level user, or a restricted administrator account, this is where we escalate to full root

/
system level access. This includes UAC bypass, elevation scripts, local exploits, brute forcing, etc

7
)
Persistance: This is where we install backdoors to secure our access. We don

't want to have to go through the whole steps above again. Things like adding local administrator accounts, setting service to start automatic on boot, putting a pinhole in the firewall service, etc

8) Root Loot scripts: This is where we search the whole system with system/root access for interesting data. This includes stealing hashes from LSA, configuration scripts, SAM/shadow database, cracking MD5 and NTLM, checking currently connected users, checking relationship between this host and other hosts, etc

9) Cleanup: This is where we scrub logfiles, clean exploits, hide backdoors, essentially we "wipe our fingerprints" from the system

10) Update maps and diagrams, and move to another system on point 3)



# From https://www.securitysift.com/offsec-pwb-oscp/

Script your enumeration

You’ll likely develop several custom scripts and use a variety of tools when enumerating in the lab.  I chose to tie all of these together into one comprehensive script that could be launched against one or many targets.  Here a basic overview of what my script did:

    TCP/UDP nmap scans to identify open ports/services for additional enumeration (see below)
    DNS enumeration (via dig)
    HTTP/S enumeration (via additional nmap scans and web file/directory brute forcing)
    MS-SQL enumeration (via nmap)
    SSH enumeration (account guessing via Hydra)
    SNMP enumeration (via nmap and onesixtyone)
    SMTP enumeration (via nmap and custom account guessing scripts)
    SMB enumeration (via samrdump)
    FTP enumeration (via nmap and hydra)

Of course you’re only limited by your imagination and scripting skills so I’m sure there are plenty of additional enumeration steps that you might think of automating. For me, the key was identifying the minimum tasks I wanted to perform while considering time and exam limitations (you won’t be able to use automated vulnerability scanners such as Nexpose, Nessus, etc). As a result I made sure to craft the script to only run the applicable enumeration scripts (based on running services) and omitted automated vulnerability tools.  Having a single script that orchestrates and formats the output for all of these various scans saved me a ton time. When it came time for my exam this proved especially useful because the exam guide gave specific instructions for one of the target systems and while I was working on that system I launched my enumeration script against the rest of the target IPs.  By the time I had gotten root on my first exam system, enumeration had completed for the rest.

Per request, I’m providing my enumeration scripts below.  Please note that these scripts come as-is with no promise of accuracy and no intent to update.


Linux privilege escalation can be a complicated task as there are so many possible vectors. Running commands one-by-one is tedious and time-consuming, especially when you have to repeat it across many systems. Again, this was another prime opportunity to leverage the power of automation.

Here’s an overview of what my Linux privilege escalation script identified:

    Basic system info (OS/Kernel/System name, etc)
    Networking Info (ifconfig, route, netstat, etc)
    Miscellaneous filesystem info (mount, fstab, cron jobs, etc)
    User info (current user, all users, super users, command history, etc)
    File and Directory permissions (world-writeable files/dirs, suid files, root home directory)
    Files containing plaintext passwords
    Interesting files, processes and applications (all processes and packages, all processes run by root and the associated packages, sudo version, apache config file, etc)
    All installed languages and tools (gcc, perl, python, nmap, netcat, wget, ftp, etc)
    All relevant privilege escalation exploits (using a comprehensive dictionary of exploits with applicable kernel versions, software packages/processes, etc)

I wrote it in python and uploaded it to each Linux system I compromised to automate all of my enumeration actions and if necessary, privilege escalation exploit discovery.  Per request, I’ve included a copy of the script for download below. Note that this script come as-is with no promise of accuracy and no intent to update.