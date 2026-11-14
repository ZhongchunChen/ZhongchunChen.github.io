SITE = {
    "name": "Zhongchun Chen",
    "role": "Undergraduate Researcher",
    "affiliation": "Shanghai Jiao Tong University",
    "location": "Shanghai, China",
    "email": "pocket-chen@sjtu.edu.cn",
    "github": "https://github.com/ZhongchunChen",
    "scholar": "#",
    "cv": "#",
    "linkedin": "#",
    "x": "#",
    "avatar": "assets/img/ZhongchunChen.jpg",
    "intro": (
        "Hi there! Welcome to my home page. My name is Zhongchun, though I "
        "usually go by Pocket. I am broadly interested in artificial "
        "intelligence and robot learning, and specifically in "
        "Vision-Language-Action (VLA) models, active perception, flow "
        "matching, and reinforcement learning (RL). I am currently an "
        "undergraduate student at Shanghai Jiao Tong University."
    ),
    "interests": [
        "Robot Learning",
        "Generative Model",
        "Representation Learning",
    ],
}

UPDATES = []

PUBLICATIONS = [
    # {
    #     "title": "Sample Publication Title on Reinforcement Learning",
    #     "authors": "Zhongchun Chen, Collaborator A, Collaborator B",
    #     "venue": "Manuscript / Conference, 2026",
    #     "description": (
    #         "A concise placeholder summary of the problem, method, and main "
    #         "result. Replace this with your accepted or submitted publication."
    #     ),
    #     "image": "assets/img/project-rl.svg",
    #     "links": {"paper": "#", "code": "#"},
    #     "tags": ["pub", "rl"],
    # },
]

PROJECTS = [
    {
        "title": "Goal-Conditioned VLA based on pi_0.5",
        "period": "2025.09 - 2025.12",
        "description": (
            "Developed a goal-conditioned robotic grasping system combining "
            "YOLO11-Seg with the pi_0.5 VLA model. Resolved the VLA model's "
            "high sensitivity to text prompts by introducing an explicit visual "
            "anchoring mechanism, significantly boosting grasping reliability "
            "on a physical FR3 robot."
        ),
        "image": "assets/img/reliable_grasp.png",
        "url": "reliable_grasp/",
        "video": "assets/content/projects/reliable_grasp_demo.mp4",
        "links": {"demo": "reliable_grasp/"},
        "tags": ["robotics", "vla", "grasping"],
    },
]

REWARDS = [
    # {
    #     "title": "Academic Scholarship",
    #     "date": "2025",
    #     "description": "Placeholder award entry. Replace with your actual scholarship or honor.",
    # },

]

EDUCATION = [
    {
        "school": "Shanghai Jiao Tong University",
        "degree": "B.Eng. / B.S. in School of Computer Science",
        "period": "2024 - Present",
        "details": "",
    },
]

EXPERIENCE = [
    {
        "organization": "SJTU HIROL-Lab",
        "url": "hirol.sjtu.edu.cn",
        "role": "Research Intern",
        "period": "2025 - Present",
        "details_html": (
            "Working on research in robot learning, including "
            "<strong>Vision-Language-Action models (VLAs)</strong>, "
            "<strong>active perception</strong>, and "
            "<strong>flow matching</strong>. Advised by "
            "<a href=\"https://lianwenzhao.github.io/\">Prof. Wenzhao Lian</a> "
            "and previously collaborated closely with "
            "<a href=\"https://ht-leung.github.io/\">Haotian Liang</a>."
        ),
    },
    {
        "organization": "NUS LinSLab",
        "url": "https://linsats.github.io/",
        "role": "Summer Research Intern",
        "period": "2026.07 - 2026.09",
        "details_html": (
            "Worked on training a general <strong>trajectory-conditioned</strong> dexterous "
            "policy using large-scale simulation data as a prior."
        ),
    },
    {
        "organization": "RoboScience",
        "url": "https://en.roboscience.co/",
        "role": "Summer Research Intern",
        "period": "2026.07 - 2026.09",
        "details_html": (
            "<strong>Led</strong> the development of a "
            "<strong>simulation platform</strong> and "
            "<strong>data pipeline</strong> for generating motion-planning "
            "data at scale based on <strong>T(R,O)</strong> dexterous "
            "grasping policy."
        ),
    },
]

NOTES = [
    {
        "title": "Flow-Matching Note",
        "date": "2026-05-19",
        "summary": "flow matching and diffusion generative model's mathematical principles.",
        "image": "assets/img/flow_matching_note.png",
        "tags": ["flow matching", "learning note"],
        "url": "notes/flow_matching_note.pdf",
    },
    {
        "title": "RL Note",
        "date": "2026-03-20",
        "summary": "Math Foundation of Reinforcement Learning",
        "image": "assets/img/RL_note.png",
        "cover_fit": "contain",
        "tags": ["RL", "learning note"],
        "url": "notes/rl_note.pdf",
    },
]

COURSES = [
    {
        "title": "CampusDB: Full-Stack Database Implementation",
        "date": "2026.11",
        "summary": "NIS3351-02 Principles of Databases course project.",
        "image": "assets/img/NIS3351.png",
        "tags": ["SJTU", "course project"],
        "url": "https://github.com/MingchenDai/NIS3351-02",
    },
    {
        "title": "Schedule Manager",
        "date": "2025-07-22",
        "summary": "NIS1336 Programming Practice: Courese Project",
        "image": "assets/img/SJTU_NIS1336_course_project.png",
        "cover_fit": "contain",
        "cover_zoom": True,
        "tags": ["SJTU", "course project"],
        "url": "https://github.com/R1bosome-He/schedule_manager",
    },
    {
        "title": "Rumor Detection System",
        "date": "2026-06-22",
        "summary": "NIS4307: Introduction to Artificial Intelligence Courese Project",
        "image": "assets/img/SJTU_NIS4307-01_course_project.png",
        "tags": ["SJTU", "course project"],
        "url": "https://github.com/ZhongchunChen/NIS4307-01",
    },
]

LIFE_RECORDS = [
    {
        "title": "Shenzhen (深圳)",
        "date": "2026.07",
        "summary": (
            "My internship brought me to Shenzhen for the first time. This "
            "photo captures an afternoon walk through a park. [2026.07]"
        ),
        "image": "assets/img/shenzhen00.jpg",
        "tags": ["Photo"],
        "url": "#",
    },
    {
        "title": "Shexian, Huangshan (黄山歙县)",
        "date": "2026.07",
        "summary": (
            "My first trip with my better half took us to this slow-paced "
            "county town, where we shared an unforgettable journey. The photo "
            "shows a local Shexian DIY craft—can you guess which one is mine? "
            "[2026.07]"
        ),
        "image": "assets/img/shexian00.jpg",
        "tags": ["Photo", "Travel"],
        "url": "#",
    },
    {
        "title": "Guilin + Liuzhou (桂林 + 柳州)",
        "date": "2025.08",
        "summary": (
            "A journey through the mountains and waters of Yangshuo in Guilin "
            "and Liuzhou. [2025.08]"
        ),
        "image": "assets/img/yangshuo00.jpg",
        "tags": ["Photo", "Travel"],
        "url": "#",
    },
    {
        "title": (
            "NIMO — Network & Information Management Organization "
            "(SJTU 网管部)"
        ),
        "date": "2024.09",
        "summary": (
            "I joined Shanghai Jiao Tong University's Network & Information "
            "Management Organization during my freshman year, where I met a "
            "group of fascinating people and picked up plenty of useful—and "
            "occasionally unusual—networking knowledge. [2024.09]"
        ),
        "image": "assets/img/nimo.jpg",
        "tags": ["Hobby", "Social"],
        "url": "https://nimo.sjtu.edu.cn/kaleid/oscope/home",
    },
    {
        "title": "Lunar New Year Atmosphere (年味)",
        "date": "2025.01",
        "summary": (
            "Festive red lanterns lit up my hometown of Dehua, filling the "
            "streets with the warmth and spirit of the Lunar New Year. "
            "[2025.01]"
        ),
        "image": "assets/img/dehua00.jpg",
        "tags": ["Photo"],
        "url": "#",
    },
    {
        "title": "20.25 km Running",
        "date": "2025.01",
        "summary": (
            "On January 1, 2025, I attempted my first near-half-marathon run—"
            "an exhilarating and deeply satisfying experience. I will always "
            "remember the support and help of my two dear friends, SF Huang "
            "and Jackie Chan. [2025.01]"
        ),
        "image": "assets/img/2025run.jpg",
        "tags": ["Hobby"],
        "url": "#",
    },
    {
        "title": "Volunteer Teaching in Gansu, China (中国甘肃支教)",
        "date": "2025.08",
        "summary": (
            "Together with 11 fellow volunteers, I spent two unforgettable "
            "weeks with high school students from three classes at Tunzi "
            "Middle School in Qingyang, Gansu. [2025.08]"
        ),
        "image": "assets/img/teach.jpg",
        "tags": ["Social"],
        "url": "https://mp.weixin.qq.com/s/RZ-yJjBCxCUL_Tk-yWHzkQ",
    },
    {
        "title": 'Red Comet Robot (“红色彗星”机器人)',
        "date": "2024.10",
        "summary": (
            "During my first semester of college, I participated in the "
            "RoboMaster campus competition, which marked the beginning of my "
            "journey exploring robotics. [2024.10]"
        ),
        "image": "assets/img/robot_game.jpg",
        "tags": ["Hobby"],
        "url": "#",
    },
    {
        "title": "Travel in Western Sichuan (川西)",
        "date": "2024.08",
        "summary": (
            "I set out alone to experience the beauty of nature with five "
            "people I had never met before. We later became close friends and "
            "have remained so ever since. [2024.08]"
        ),
        "image": "assets/img/sichuan00.jpg",
        "tags": ["Travel", "Photo"],
        "url": "#",
    },
]
