import streamlit as st

st.title("Behavior questions")

tab1, tab2, tab3, tab4 = st.tabs(["Introduction", "Management Skills", "Digital Human", "Web Table"])
with tab1:
    with st.expander("Introduction."):
        st.write("""Hello, I’m Hongjun. I have over ten years of experience in the software engineering industry, specializing in machine learning and large-scale system architecture. Currently, I’m working at CloudWalk Technology in Shanghai, where I lead teams in developing AI products. My work includes developing LLM-based Knowledge Engines, as well as creating an AIGC product that integrates digital human and LLM for video creation and e-commerce live streaming.\n
Before CloudWalk, I worked at Google in New York as a Tech Lead Manager. There, I led the development of Search Architecture and launched several key Google search products. One of my major accomplishments was building a machine learning-based web table platform, which became a key data source for the Google Knowledge Graph.\n
Earlier in my career, I worked at Bloomberg as a Tech Lead, where I designed and implemented the Bloomberg Legal Platform, integrating services to support legal, news, and financial research.\n
I’m passionate about leveraging AI to solve complex problems and build scalable solutions that have a real-world impact.""")

    with st.expander("Expectation."):
        st.write("""I’m looking for a role at the Senior Engineering Manager or Director level, ideally focused on developing LLM or Generative AI related products. I’d prefer to lead a team, but if a management role isn’t available, I’m also open to starting in an IC role. If I’m not overseeing the entire product, I’d like to take charge of a key component of it.""")

    with st.expander("Management experience."):
        st.write("""I spent five years at Google, and about three years in, I became a people manager. By the time I left, my team had grown to around 15 engineers, split into two sub-teams, with a few individual contributors reporting directly to me.\n
At CloudWalk, my responsibility expanded further. My team grew from around 30 to 50 people, including engineers, machine learning specialists, product managers, designers, and project managers. I managed 4 sub-teams, one focused on infrastructure, one on machine learning engineering, and two on product development. Besides that, I had about 5 individual contributors reporting directly to me.""")

    with st.expander("Machine learning experience."):
        st.write("""I began working on machine learning projects as soon as I joined Google, and one of my major contributions was developing a machine learning-based web table platform. There are an immense number of tables on the internet, with approximately one in every two web pages containing a table. We used machine learning to extract and understand these web tables. To better identify tables on web pages, we applied vision-based machine learning algorithms. Then, we leveraged early LLMs like BERT and T5 to enhance our understanding of the tables. This included classifying the tables, identifying the ones most relevant to the web page's topic, and generating appropriate titles for them. The information extracted from these tables became a key data source for Google’s knowledge graph and was later integrated into other products like Google Search, Google Maps, and YouTube.\n
After I joined CloudWalk, I continued leading the Knowledge Engine team. My team developed two key products: one was a knowledge engine based on large language models, and the other was an AIGC platform that integrated these models with digital humans. The knowledge engine extracts information from documents to build knowledge graphs, which are then used to enhance retrieval augumented generation (RAG). On the AIGC platform, we helped users create e-commerce live-streaming scripts and dialogues, and enabled real-time interactions with viewers through large language models. To ensure our products performed well, we carried out extensive data processing and fine-tuned the models using machine learning techniques.""")

    with st.expander("Performance review experience."):
        st.write("""Google’s performance evaluation system is quite structured and thorough. It begins with a self-assessment, followed by peer reviews and a manager’s evaluation. To keep things fair and consistent across teams, managers hold calibration sessions to agree on a rating for each employee. Once the ratings and evaluations are finalized, the manager sits down with the employee to go over the results and provide feedback.\n
At CloudWalk, our approach is more flexible and less formal compared to Google’s. We focus on setting goals and providing continuous feedback. While we do discuss ratings within teams inside a department, we don’t have cross-department calibration meetings.""")

    with st.expander("Why do you want to go back to US?"): 
        st.write("""I decided to move back to China two years ago for both personal and professional reasons. On the personal side, at that time, China had effective COVID-19 control measures in place, which made it a safer environment for my family. Professionally, I had the chance to join CloudWalk, an AI company that was preparing for an IPO. It was an exciting opportunity to be part of a fast-growing company in the AI space.\n
Now, I’m looking to return to the U.S. because we've decided to have our child receive an education here, and personally, I prefer the American lifestyle. I also believe the U.S. continues to lead global innovation in AI, and I want to be part of that cutting-edge environment to contribute to and learn from the advancements being made.""")

    with st.expander("Why did you transfer to computer science?"):
        st.write("""When I was an undergraduate, a teacher sparked my interest in quantum computing by predicting we’d have quantum computers within 15 years. This inspired me to pursue quantum information as my research area. However, as I delved deeper into the field, I realized that achieving functional quantum computers could take much longer—possibly 50 years or more.\n
I wanted to work on something that could have a more immediate impact on the real world. Since I had already studied computer science-related courses and wrote code for my research, transitioning to computer science felt like a natural move. I started at Bloomberg, where I had the opportunity to work on search engines, and later joined Google, continuing my work on Search and moving into machine learning projects.\n
With the rise of large language models (LLMs) and Generative AI, I’ve found my true passion: using AI to solve complex problems and build scalable solutions that have a tangible, real-world impact.""")

    with st.expander("Expected Compensation."):
        st.write("""Based on my research and understanding of the industry standards for this role, along with my skills and experience, I would expect a compensation range between 400K and 700K. This range reflects the value I can bring to the position and is aligned with current market rates. However, I’m open to discussing the full compensation package, including benefits and other forms of compensation, to find a mutually agreeable arrangement.""")

    with st.expander("Why do you want to step back to lead only one team?"):
        st.write("""I’ve been overseeing four sub-teams in China, which has been a valuable experience. However, as I’m planning to return to the U.S., my focus isn’t necessarily on managing multiple teams, but on working on projects that are both interesting and impactful. The U.S. is leading the AI trend, and I’m excited to be a part of cutting-edge developments, even if that means managing a smaller team.\n
In my view, the quality of the work and the opportunity to make a significant impact matter more than the size of the team. If I’m working on an exciting project that pushes boundaries and drives real-world results, I’ll be just as motivated and invested as I’ve always been.""")

    with st.expander("Why do you want to join Capital One?"):
        st.write("""I’m excited about the opportunity at Capital One because the company is a leader in combining finance and technology to innovate within the banking industry. Capital One’s commitment to being a “tech company that happens to be in finance” really resonates with me, as it highlights the importance of data-driven decisions and cutting-edge technology, particularly in AI/ML.\n
I’m particularly drawn to the role because it provides a chance to leverage my experience in machine learning to solve impactful problems in finance, like fraud detection, customer personalization, and credit risk management. Capital One’s focus on innovation and continuous learning also aligns with my passion for driving advancements in AI/ML, and I’m excited to contribute to pushing those boundaries in the financial space.""")

with tab2:
    st.header("Meta specific questions")
    with st.expander("Why do you want to join Meta?"):
        st.write("""1. **Meta is leading in AI innovation**: I want to join Meta because it’s driving breakthroughs in AI and machine learning that impact billions of people. The work in areas like recommendation systems, augmented reality, and large language models fits perfectly with my experience and passion.\n
2. **Meta's Commitment to openness and collaboration**: I admire Meta’s approach to open-sourcing models like Llama, which helps the AI community grow and innovate together. In many ways, Meta has become the “real OpenAI,” fostering transparency and accessibility while advancing cutting-edge research.\n
3. **Excited to contribute to Meta’s mission**: As a Machine Learning Engineering Manager, I’m eager to lead teams and work on projects that shape the future of social connections and digital experiences. Meta’s mission of connecting people through technology deeply resonates with me, and I’m excited about the chance to lead teams that will make a meaningful difference in that vision.""")

    with st.expander("What questions do you have for me?"):
        st.write("""Company Culture and Values:\n
- "Can you describe the company culture and what it’s like to work here day-to-day?"\n
- "How does the company support professional development and career growth?"\n
Role and Expectations:\n
- "What are the key challenges and opportunities for ML engineering manager in the first six months?"\n
- "How do you measure success of a ML engineering manager, and what are the primary goals for the person in this role?"\n
Team Dynamics:\n
- "Can you tell me more about the team I would be working with and how they collaborate?"\n
- "How does the team handle conflicts or differing opinions?"\n
Company Goals and Vision:\n
- "What are the company’s short-term and long-term goals, and how does this role contribute to achieving them?"\n
- "How has the company’s strategy evolved recently, and what are the key initiatives for the upcoming year?"\n
Next Steps:\n
- "What are the next steps in the hiring process, and when can I expect to hear back?""")

    with st.expander("Meta values a strong feedback culture. How do you give and receive feedback?"):
        st.write("""I believe feedback is essential for growth, both at an individual and team level. Here’s how I approach giving and receiving feedback:\n  
Giving Feedback:\n
1. Be Specific and Constructive: When providing feedback, I focus on specific behaviors or outcomes, not personal attributes. For example, instead of saying, “Your code isn’t good,” I would say, “The recent implementation could be optimized for scalability by refactoring this module.”\n  
2. Timeliness: I give feedback as close to the event as possible, whether it’s positive or constructive, so it’s relevant and actionable.  \n
3. Balance: I ensure a balance of positive reinforcement and areas for improvement. Highlighting what’s working well keeps morale high, while constructive feedback helps people grow.\n
4. Collaborative Approach: I frame feedback as a dialogue. For instance, I might ask, “How do you think this approach worked? Is there something we could adjust?” to encourage self-reflection and mutual problem-solving.\n  
Receiving Feedback:\n
1. Be Open-Minded: I view feedback as an opportunity to learn and improve. Even when the feedback is unexpected or challenging, I focus on understanding the perspective rather than reacting defensively.\n  
2. Seek Clarity: I ask clarifying questions to ensure I understand the feedback fully, such as, “Can you provide an example so I can better address this?”  \n
3. Take Action: I prioritize acting on feedback and communicating my progress. For instance, when I received feedback about improving communication with non-tech stakeholders, I took actions like simplifing technical concepts, using diagrams, and encouraging open dialogue. This quickly improved alignment and collaboration.\n  
4. Create a Feedback Loop: I encourage my team and peers to provide regular feedback. This builds a culture of trust and continuous improvement.  \n
At Meta, where feedback is integral, my approach would align well with fostering a collaborative and growth-oriented team environment.""")

    with st.expander("If you have unlimited resources, what feature do you want to implement for meta?"):
        st.write("""If I had unlimited resources, I would build a Knowledge-Powered AI Assistant with Long-Term Memory and Personalization that seamlessly integrates across Meta’s platforms. This agent would leverage advancements in generative AI, multimodal interactions, and cross-platform integration, while drawing from my expertise in search, knowledge graphs, and digital human technologies.\n  
Feature Overview:\n
The AI assistant would act as a highly personalized digital companion, capable of assisting users in a wide range of tasks:\n  
1. Long-Term Memory: The agent would retain contextual knowledge about users over months or years, enabling it to evolve with their needs. For example, it could remember a user’s interests, past interactions, and ongoing goals, offering tailored recommendations and insights.\n  
2. Personalization: Using advanced AI and knowledge graph technologies, the agent would dynamically adapt to users’ preferences, whether it’s curating content, facilitating social connections, or assisting with productivity tasks.  \n
3. Knowledge-Powered Intelligence: With a robust foundation in search and structured data from knowledge graphs, the agent would provide accurate and actionable responses, acting as both a conversational partner and a reliable information source.\n  
4. Generative and Multimodal Interaction: The agent would support text, voice, video, and even digital human-based communication, ensuring a seamless and immersive experience across Meta’s platforms (Facebook, Instagram, WhatsApp, Horizon, etc.). \n 
5. Cross-Platform Synchronization: It would integrate across devices and Meta's ecosystem, allowing users to pick up conversations or tasks wherever they are.  \n
Why This Feature?\n
1. Stronger User Engagement: By offering deeply personalized and context-aware interactions, the agent would create stronger user connections to Meta’s platforms.\n  
2. Alignment with Meta’s Vision: This feature fits perfectly with Meta’s focus on building the metaverse, enabling AI-driven, immersive, and interconnected experiences.\n  
3. Empowering Users: It would help users navigate complex information, streamline daily tasks, and create meaningful interactions, enhancing their digital lives.  \n
Implementation with Unlimited Resources:\n
1. Cutting-Edge Research: Invest in long-term memory architectures for AI models and new techniques to enhance personalization through user-contextual data.\n  
2. Knowledge Infrastructure: Expand Meta’s existing search and knowledge graph capabilities to power the AI with high-quality, structured data.  \n
3. Ethics and Privacy: Develop advanced mechanisms to ensure privacy, user consent, and ethical AI usage while maintaining transparency.  \n
4. Scalable Infrastructure: Build a scalable platform capable of handling billions of users with multimodal and real-time interactions.  \n
This AI assistant would be a transformative feature for Meta, combining personalization, knowledge, and immersive interaction to redefine how users experience the digital world.""")

    with st.expander("What excites you most about the challenges at Meta compared to your previous roles?"):
        st.write("""Meta's unique combination of innovation, scale, and speed makes its challenges particularly exciting compared to my previous roles. While Meta shares similarities with Google, where I worked as a Tech Lead Manager, it stands out in several key ways:\n
1. Commitment to Open Source Leadership:Meta’s active contributions to the open-source community, from PyTorch to Llama, are incredibly inspiring. PyTorch has become a cornerstone of modern machine learning research and development, while Llama showcases Meta's commitment to democratizing access to advanced language models. This open-source-first mindset not only accelerates innovation within the industry but also demonstrates Meta's willingness to lead and share at a global scale.\n  
2. Agility and Speed:Meta’s ability to move faster than many large companies, including Google, is a huge draw. The company's iterative, experiment-driven approach fosters rapid innovation and empowers teams to test, learn, and deploy solutions quickly. This speed is critical in areas like machine learning, where staying ahead of the curve is essential.\n
3. Integration of Research and Applications:Meta excels at integrating cutting-edge research directly into its products at scale. For instance, applying generative AI in creative tools for Instagram or leveraging advanced recommendation algorithms for Facebook ensures that research doesn’t stay in the lab but impacts billions of users daily.\n
4. Diverse Challenges Across Products:Meta’s portfolio—from social platforms like Instagram and Facebook to immersive experiences in Reality Labs—offers a breadth of challenges. These opportunities span personalization, AR/VR, and AI-driven content creation, all areas that align with my experience and passion for solving complex problems.\n
Meta’s open-source leadership, speed of execution, and ability to balance cutting-edge research with real-world impact make it an incredibly exciting place to take on new challenges. These qualities align closely with my passion for leveraging ML to build scalable, impactful solutions.""")

    with st.expander("How do you think Meta’s approach to machine learning sets it apart from other companies?"):
        st.write("""Meta’s approach to machine learning stands out due to its focus on innovation at scale, integration across products, and openness to collaboration. Here’s what I find particularly unique:\n
1. End-to-End Integration Across Products:\n
 - Unlike many companies that focus on siloed ML applications, Meta integrates ML deeply into its ecosystem, from content ranking in Facebook feeds to AR effects in Instagram and advancements in Reality Labs. This holistic approach ensures consistency, personalization, and scalability across all platforms.\n
2. Focus on Personalization and Real-Time Systems:\n
 - Meta’s commitment to delivering personalized user experiences, powered by real-time ML systems, is unparalleled. Managing such massive-scale personalization systems requires tackling latency, scalability, and contextual relevance, which Meta does exceptionally well.\n
3. Research-Driven Innovation:\n
 - Meta AI invests heavily in foundational research, contributing to advancements in areas like self-supervised learning, large language models, and generative AI. Initiatives like PyTorch and FAIR (Facebook AI Research) demonstrate a commitment to pushing the boundaries of ML and sharing innovations with the broader community.\n
4. AI Infrastructure and Efficiency:\n
 - Meta’s focus on building state-of-the-art ML infrastructure ensures that its models are not only powerful but also efficient. For instance, innovations in model compression and distributed training make it possible to deploy advanced models in real-world applications at scale.\n
5. Open Collaboration with the Community:\n
 - Meta’s contributions to the open-source community, such as PyTorch and open research publications, foster collaboration and accelerate progress in ML globally. This ethos of openness is inspiring and underscores Meta’s leadership in the field.\n
6. Emphasis on Ethical AI:\n
 - Meta’s initiatives to build responsible and ethical AI, addressing issues like bias and transparency, reflect a forward-thinking approach to deploying ML at scale. Balancing innovation with responsibility sets it apart from many competitors.\n
Meta’s ability to combine cutting-edge research with practical applications across its vast ecosystem makes its ML approach uniquely impactful and exciting.""")

    with st.expander("Meta's core value: Move fast."):
        st.write("""Situation:\n
When we started promoting our digital human live-streaming product, we landed a major client—a large chain brand with over 100 stores. They needed individual accounts for each store and requested a centralized management system. This system had to enable them to manage permissions for each store, monitor account usage, and view various statistics. To secure this high-value client, we had to develop the system urgently.\n
Task:\n
My task was to quickly lead the team in designing and building this management system while ensuring we met the client’s tight timeline without compromising on quality.\n
Action:\n
To move fast, I immediately gathered a cross-functional team, including engineers and product managers, to define the scope and prioritize the most critical features. Instead of creating a complete system from the ground up, we used existing parts from our platform to speed up the development process. Specifically, we adapted features from our internal management system, enabling clients with multiple accounts to manage their accounts effectively. I set up daily stand-ups to monitor progress, remove blockers, and ensure alignment. Additionally, I worked closely with the client to clarify requirements and iterate quickly on the design to meet their needs.\n
Result:\n
Within just one month, we delivered a functional management system that met the client’s requirements. This secured the deal with the client, who became one of our most important customers, and the system later became a key feature that attracted similar enterprise clients. By acting with urgency and focusing on the highest-priority tasks, we not only retained the client but also enhanced our product offering.""")

    with st.expander("Meta's core value: Build awesome things.(The digital huamn project.)"):
        st.write("""**Situation:**\n  
At CloudWalk, I led the development of a digital human live-streaming product designed to revolutionize the live-streaming e-commerce industry. Traditional live hosts were expensive, and the barriers to entry for small businesses were high. We aimed to build a solution that was not just functional but also inspiring—enabling businesses to create engaging, personalized digital hosts and automate key parts of the live-streaming process.\n  
**Task:**  \n
My goal was to create a product that would amaze users by combining cutting-edge AI technologies like large language models, real-time rendering, and interactive features, all while ensuring the solution was cost-effective and easy to use.\n  
**Action:**  \n
To achieve this, I focused on three aspects:\n  
1. **Innovated in Real-Time Rendering:** Optimized the rendering engine pipeline and built a dedicated scheduling center to enable real-time, high-quality digital avatar rendering using consumer-grade GPUs.\n  
2. **Enhanced User Experience:** Integrated a script-generation feature powered by fine-tuned large language models, allowing users to create professional live-streaming scripts effortlessly. We enabled real-time editing and used user feedback to improve the model continuously.\n  
3. **Pioneered Interactive Features:** Built an automated Q&A system using Retrieval-Augmented Generation (RAG), which could extract relevant information from uploaded files and respond to audience questions in real time, creating a highly engaging experience.  \n
**Result:**  \n
The product became a game-changer for the industry, empowering over 10,000 paying users and generating tens of millions of dollars in annual revenue. It wasn’t just useful—it inspired businesses by making professional live-streaming accessible to everyone. The mix of cutting-edge technology and a simple, user-friendly design amazed our clients, making the product one of the company’s top highlights.""")

    with st.expander("Meta's core value: Build awesome things. (Another example: generating reports.)"):
        st.write("""**Situation:**  \n
During the development of our digital human live-streaming product, we discovered through conversations with merchants that their teams spent significant time after each live stream analyzing what went well and what could be improved. This process was labor-intensive and often lacked actionable insights. To address this, we decided to develop a feature that would automatically generate a comprehensive post-stream analysis report.\n  
**Task:**  \n
The goal was to create a feature that not only provided basic live-stream metrics—such as peak viewers and best-selling products—but also leveraged large language models to analyze and summarize the live-stream content, including speech and audience interactions.\n  
**Action:**  \n
To build this feature, I focused on three key aspects:\n  
1. **Integrated Data Analytics:** Designed a system to capture and analyze key metrics from each live stream, such as viewer engagement and product performance.\n  
2. **Utilized Large Language Models:** Implemented an AI-driven summary tool to review the live-stream script and interaction logs. This tool categorized audience questions, highlighted unanswered ones, and allowed users to add responses, improving future live streams.\n  
3. **Enhanced User Experience:** Made the summaries actionable by providing merchants with clear insights and suggestions, enabling them to address gaps and optimize their future streams. We also iterated rapidly based on user feedback to ensure the feature met real-world needs.\n  
**Result:**  \n
The post-stream analysis feature became a standout capability of our product, saving merchants hours of manual work and providing them with actionable insights to improve their next live streams. Merchants were particularly impressed by the AI-driven summaries of audience questions, which helped them better address customer needs. This feature contributed significantly to the product’s success, attracting new clients and reinforcing our reputation for innovation.""")

    with st.expander("Meta's core value: Be direct and respect your colleagues.(Conflict between pm and engineer.)"):
        st.write("""To answer this question, you should provide an example where you demonstrated the ability to have a direct, respectful conversation or provide constructive feedback, even in a challenging situation. Use the **STAR method** (Situation, Task, Action, Result) to structure your response. Highlight how you balanced being straightforward with maintaining respect and professionalism.\n
**Situation:**  \n
During the development of our digital human live-streaming product, we encountered a major conflict between the product manager and the engineering team. The product manager was eager to integrate a large language model into our system as soon as possible, seeing it as a critical market differentiator. While the engineering team fully agreed on the importance of this feature, they had serious concerns about the feasibility of the proposed timeline. This difference in priorities created tension and risked delaying the project.\n  
**Task:**  \n
As the leader of the team, my task was to address the conflict head-on, facilitate a resolution, and ensure the team could move forward with clarity and alignment.\n  
**Action:**  \n
I organized a meeting with both the product manager and the engineering leads. In the meeting:\n  
1. **Acknowledged Expertise:** I began by recognizing the product manager’s vision and the engineering team’s technical expertise, emphasizing the value each brought to the project.\n  
2. **Encouraged Open Dialogue:** I encouraged everyone to voice their concerns openly but respectfully. I made it clear that the goal was to find a solution together, not to assign blame.\n  
3. **Proposed a Compromise:** After understanding both sides, I suggested breaking the project into phases. In the first phase, we would implement a smaller-scale integration of the large language model to validate the concept. This approach addressed the product manager’s need for differentiation while giving the engineering team time to overcome technical challenges in subsequent phases.\n  
4. **Followed Up:** After the meeting, I checked in with both sides individually to ensure they felt heard and supported.  \n
**Result:**  \n
The phased approach was accepted by both parties, and the project moved forward without further delays. The initial phase was completed successfully, and the subsequent phases benefited from the engineering team’s additional preparation time. The respectful and constructive resolution also strengthened the team’s trust and collaboration, fostering a more open culture for future discussions.  """)

    with st.expander("Meta's core value: Focus on long-term impact."):
        st.write("""""")

    with st.expander("Meta's core value: Live in the future.(Leverage Digital human to promote our product.)"):
        st.write("""**Situation:**  
To promote our digital human live-streaming product, we decided to leverage Douyin (China’s mainstream social media platform, similar to TikTok) and other social media platform to attract small and medium-sized merchants. The goal was to demonstrate the product’s potential while also gaining insights into user needs by using the product ourselves.  
**Task:**  
My task was to design and execute a strategy where we used digital humans to create engaging content and host live streams on Douyin, showcasing the capabilities of our product. This initiative aimed to drive user acquisition while also improving our product based on real-world feedback.  
**Action:**  
1. **Created a Digital Human Account:** We launched a dedicated Douyin account, using our digital human technology to produce high-quality videos and host live-streaming sessions. These videos introduced our product’s features, demonstrated its use cases, and engaged directly with potential customers.  
2. **Acted as Early Adopters:** By running the account ourselves, we placed ourselves in the shoes of our target users. This allowed us to experience firsthand the challenges and opportunities merchants might face when using our product.  
3. **Iterated Based on Feedback:** Through this process, we identified areas for improvement, such as enhancing the script generation feature and optimizing the live-streaming interface. These insights were fed back into our development cycle to make the product more user-friendly and effective.  
4. **Engaged with the Community:** We actively interacted with followers in the comments and during live streams, building trust and a sense of community around our product.  
**Result:**  
The campaign was a great success. Over half of our new users were acquired through the Social media account, significantly boosting our user base. Additionally, by using our product as early adopters, we improved its usability and ensured it met the needs of our target audience. This initiative not only showcased the future of digital human technology but also strengthened our product’s market position.  
---
**Why This Answer Works:**  
1. **Forward-Looking Approach:** Demonstrates how you embraced the future of digital human technology and social media marketing.  
2. **Early Adoption:** Highlights your willingness to use your product to gain insights and drive improvement, embodying the principle of "living in the future."  
3. **Impact:** Quantifies the success of the initiative in terms of user acquisition and product improvement.  
4. **Cultural Fit:** Aligns with Meta’s value by showing how you built a forward-thinking strategy that inspired and engaged your audience.  
This example effectively illustrates your ability to adopt and shape innovative solutions, aligning with Meta’s "Live in the future" value.""")

    with st.expander("Meta's core value: Meta, Metamates, me.(Support engineer with personal challenge.)"):
        st.write("""To answer this question, you should provide an example where you demonstrated responsibility for the success of your team, company, or mission, and how you supported or took care of your teammates. Use the **STAR method** (Situation, Task, Action, Result) to structure your response, and emphasize collaboration, team support, and a sense of collective ownership.\n

---

**Example Answer:**  \n

**Situation:**  \n
During the development of our digital human live-streaming product, our team was under significant pressure to deliver a high-quality product within a tight timeline. One of our engineers was struggling to meet deadlines due to personal challenges, which began to affect the team’s overall progress.\n  

**Task:**  \n
As the leader, my responsibility was to ensure the project stayed on track while supporting the engineer and maintaining team morale. It was important to balance individual well-being with the collective success of the team and the company’s mission.\n  

**Action:**  \n
1. **Supported the Engineer:** I had a one-on-one conversation with the engineer to understand their challenges. I assured them that the team valued their contributions and offered flexible working hours to accommodate their situation.\n  
2. **Redistributed Workloads:** I worked with the team to redistribute some of the engineer’s tasks temporarily, ensuring the project timeline wasn’t compromised. I also personally took on some of the technical work to lighten the load for the team.\n  
3. **Fostered Team Collaboration:** To maintain team cohesion, I encouraged open communication and collaboration. We held daily check-ins to ensure everyone felt supported and aligned.  \n
4. **Kept the Bigger Picture in Mind:** Throughout the process, I reminded the team of our shared mission to deliver a product that could revolutionize live-streaming for small businesses, reinforcing the importance of working together.\n  

**Result:**  \n
The engineer was able to overcome their personal challenges without feeling isolated, and the team successfully delivered the project on time. The supportive environment strengthened team morale and fostered a deeper sense of trust and collaboration. The product went on to generate significant revenue and positive feedback, reflecting our collective success.\n  

---

**Why This Answer Works:**  \n
1. **Responsibility:** Demonstrates your sense of responsibility for both the team’s success and the well-being of individual teammates.\n  
2. **Teamwork:** Highlights how you fostered collaboration and supported your teammates in a challenging situation.  \n
3. **Mission Alignment:** Connects the actions to the broader mission of delivering an impactful product.  \n
4. **Cultural Fit:** Reflects the "Meta, Metamates, me" value by showing care for the company, the team, and individual members.\n  

This response illustrates how you prioritized collective success while supporting your teammates, embodying Meta’s value of "Meta, Metamates, me.""")

    st.header("Conflicts and other challenges")
    with st.expander("What systems have you put in place to resolve conflicts and maintain a healthy team dynamic?"):
        st.write("""**Situation:**  
Yeah, so in my experience leading teams, I’ve definitely seen situations where people had different opinions on technical approaches or just clashed because of different working styles. If those kinds of things aren’t handled properly, they can really impact team morale and progress.  

**Task:**  
My goal has always been to set up systems that catch issues early, promote open communication, and create a collaborative, respectful environment where conflicts don’t derail the team or the project.  

**Action:**  
What I’ve found works well is a combination of proactive communication, structured conflict resolution, and fostering team trust:  

- **Regular one-on-one check-ins:** I make time to talk individually with each team member. It’s a great way to **catch small issues early** and gives people a safe space to share feedback or concerns.  
- **Transparent team meetings:** I keep meetings **open and inclusive**, encouraging everyone to share their thoughts and ideas. The focus is on creating an environment where **constructive criticism is welcomed** and no one feels dismissed.  
- **Clear conflict resolution process:** When conflicts arise, I focus on:  
  - **Active listening** to ensure everyone gets a chance to share their perspective.  
  - **Mediating discussions** to help team members understand each other’s viewpoints.  
  - **Finding solutions** that align with the team’s goals and create a win-win whenever possible.  
- **Encouraging collaboration across roles:** For example, I’ve paired ML engineers with front-end developers to solve problems together. This approach helps build **empathy across different perspectives** and often leads to more creative solutions.  
- **Team-building activities:** I organize both formal and informal activities, like workshops or casual team lunches. These moments help **strengthen relationships and build trust** within the team.  
- **Setting clear expectations and accountability:** I make sure the team knows what’s expected in terms of communication, collaboration, and respect. And if someone’s behavior is disruptive, I address it directly but constructively.  

**Result:**  
These systems have worked really well for my teams. Conflicts get resolved quickly and don’t escalate into bigger issues. More importantly, we’ve been able to maintain a **healthy, open team dynamic** where people feel comfortable sharing their ideas. This has led to **better collaboration, stronger relationships, and successful project outcomes.**""")

    with st.expander("Tell me about a time you had to mediate a conflict inside your team.(LLM api)"):
        st.write("""While working on the digital human product, we faced a conflict between the frontend and backend engineers about how to integrate the LLM API into our system. The frontend engineer wanted to directly connect to the LLM API from the frontend, thinking it would be faster to implement and allow us to quickly showcase results. On the other hand, the backend engineer insisted that the API calls should go through the backend, like the other APIs we used, to keep things consistent and manageable.\n
As the engineering manager, I organized a meeting to hear both sides and figure out the best approach. The frontend engineer explained that direct integration would reduce development time and allow for quicker iterations. Meanwhile, the backend engineer shared concerns about scalability, security, and long-term maintainability, as well as the need to align with our existing system architecture.\n
I also brought up an additional point: if the frontend handled API calls directly, we would lose the ability to track user interactions effectively. Tracking this data is critical because it helps us understand user behavior and improve the LLM's performance based on real feedback.\n
After discussing the technical implications together, the team agreed to route the API calls through the backend. This approach ensured consistency, better scalability, and the ability to track user data. The frontend engineer was also happy with this solution because it made their work simpler. They could still directly call the LLM API during development for experiments and testing without any extra complexity.\n
By organizing this discussion and focusing on the product's long-term needs, I helped the team align on a solution. The conflict was resolved with both engineers feeling heard and satisfied, and this strengthened collaboration within the team moving forward.""")

    with st.expander("Another example of conflicts inside my team.(Script generation)"):
        st.write("""There was a conflict between our product manager and a machine learning engineer while working on the digital human live-streaming product. The product manager wanted to prioritize a feature to automatically generate live-stream scripts, believing it would save users time and make the product stand out. However, the machine learning engineer was concerned that the automatically generated scripts might not meet user expectations, leading to dissatisfaction.\n
As the engineering manager, I brought the two together to understand their perspectives. The product manager explained that adding this feature was key to differentiating our product in the market and addressing user pain points. However, the machine learning engineer expressed concerns that the current quality of the LLM-generated live-stream scripts was far from ideal. Achieving the desired results would require significant work, including improving the model and building the necessary infrastructure, which couldn’t be accomplished quickly.\n
After discussing both sides, we decided to redesign the feature and turn the "autopilot" into a "copilot." Instead of fully automating the script generation, the product would now work collaboratively with users. The system would provide a draft script based on the product and context, and users could review and refine it. This gave users control while still saving them time.\n
We took a phased approach to develop this feature. First, we built a prototype to gather user feedback, ensuring the functionality met their needs. At the same time, we focused on improving the large language model to provide better initial drafts. This solution satisfied the product manager’s goal of adding a standout feature while addressing the engineer’s concerns about quality and user satisfaction.\n
The conflict was resolved, and both sides were happy with the new direction. This collaborative approach strengthened the team and led to a more user-friendly and impactful feature.""")

    with st.expander("Tell me about a time you created alignment between individuals that also happen to be strongly opinionated.(More GenAI features.)"):
        st.write("""### **Situation**  \n
During the development of our digital human live-streaming product, the product manager strongly pushed to integrate more AIGC features as soon as possible, such as generating background photos and decorations for the virtual live-streaming room. While the idea was innovative and aligned with market trends, the engineering team had concerns about feasibility, resource availability, and the risk of delaying the core features already in progress.\n
### **Task**  \n
My role as the product lead was to align both sides on a clear path forward that balanced innovation, technical feasibility, and delivery timelines, while ensuring team motivation and focus.\n
### **Action**  \n
1. **Understand Both Perspectives:**\n  
I started by having separate conversations with the product manager and the engineering team to understand their perspectives. The product manager saw AIGC features as a way to gain a competitive edge, while the engineers were worried that adding unplanned features could delay our core roadmap and overextend resources.\n
2. **Facilitate a Structured Discussion:**  \n
To align everyone, I brought both sides together for a focused discussion. I asked the product manager to explain the market need and potential impact of the features, and then the engineers outlined the technical challenges, like the extra model development time, higher inference costs, and risks to our delivery timeline.\n
3. **Prioritize Based on Impact and Feasibility:** \n
To find common ground, I suggested we evaluate the AIGC features using two criteria: business impact and development complexity. Together, we created a simple matrix to prioritize them. For instance, generating virtual room backgrounds was high-impact and relatively simple, while real-time decoration generation was much more complex and resource-intensive.\n
4. **Propose a Phased Approach:**  \n
We agreed on a phased plan. In the short term, we focused on generating static backgrounds for virtual live-streaming rooms, as it could be implemented quickly without disrupting the roadmap. For more complex features, like dynamic decorations, we decided to revisit them in a later phase once the core functionality was delivered and stable.\n
5. **Align on Shared Goals:**  \n
Throughout the process, I emphasized our shared goal: delivering a high-quality product on time while exploring innovative features to stay ahead in the market. By ensuring both sides felt heard and showing how the phased plan balanced innovation with feasibility, we reached a solution everyone could support.\n
### **Result**  \n
Both the product manager and engineering team agreed to the phased approach. The engineering team could stay focused on delivering the core roadmap, and the product manager was satisfied that we were still prioritizing impactful AIGC features. We successfully delivered the static background generation feature in the next release, which received positive customer feedback, and we continued exploring more advanced AIGC features in subsequent phases.\n
### **Summary (Closing):**  \n
By facilitating open discussions, using a prioritization framework, and proposing a phased approach, I was able to align two strongly opinionated sides. This allowed us to deliver value quickly while maintaining focus on our core goals and ensuring the team remained motivated and productive.""")

    with st.expander("Tell me about a time you resolved a conflict between an engineer on your team and a cross-functional partner. (Rendering system)"):
        st.write("""While working on the digital human product at CloudWalk, a conflict arose between our backend architect and an engineer from the infrastructure team. The backend architect believed we needed a new resource scheduling system to support the unique requirements of digital human rendering for a consumer-facing product. The infrastructure engineer, however, felt that the existing system, designed for B2B projects, could be adapted with minor adjustments rather than a full redesign.\n
As the engineering manager, I stepped in to mediate. First, I met with both engineers individually to understand their concerns. The backend architect was focused on the need to scale for potential explosive user growth, while the infrastructure engineer wanted to avoid unnecessary complexity and costs.\n
To move forward, I also met with the manager of the infrastructure team. Together, we estimated the required resources, task complexity, and the timeline for either approach. After a thorough assessment, we agreed that redesigning the resource scheduling system was the best long-term solution for scalability and performance. We adjusted the project scope to accommodate the changes, ensuring that both teams had the resources and time needed.\n
By fostering open communication and collaborating with the infrastructure manager, we reached a solution that balanced immediate technical needs with future scalability, turning the conflict into an opportunity to build a more robust system.""")

    with st.expander("Tell me about a time you had conflicts with other team.(2D vs 3D digital human)"):
        st.write("""During the development of our digital human product, there was a debate between teams about whether we should focus more on 2D or 3D digital humans. The machine learning team had been splitting resources almost equally between the two, believing that 3D would offer more advanced capabilities, such as a higher level of realism and interactivity. However, 3D models required more complex computations and expensive hardware for rendering, making them resource-intensive and time-consuming to develop. On the other hand, 2D digital humans, based on video or images, focused primarily on lip synchronization, which made them much more efficient and technically simpler. This allowed them to be produced faster and at a lower cost, making them more practical for the immediate needs of our users.\n
After conducting market research, we found that e-commerce professionals preferred 2D digital humans because they appear more realistic, as they are derived from real video footage. Although 3D digital humans have a more high-tech and dynamic appearance, it’s pretty clear right away that they aren’t real, which made them less ideal for e-commerce live-streaming.\n
I stepped in to mediate by conducting a thorough analysis of user feedback and market trends. It became clear that 2D digital humans aligned better with what our users actually wanted in the short term and would allow us to deliver value faster with fewer resource constraints. I presented this data-backed analysis to senior management and external teams, explaining that focusing on 2D would lead to a quicker, more successful product launch, while we could still explore 3D in the future as the market evolved.\n
By keeping communication open and providing a clear comparison of the pros and cons of each approach, I was able to convince the external teams to reallocate resources towards 2D digital humans. This decision helped the project stay focused and contributed to its overall success in the market.""")

    with st.expander("Share an example of a disagreement you had with a colleague or team member. How did you approach resolving it?(Video Creation.)"):
        st.write("""In our digital human live-streaming platform project, besides live-streaming, we also wanted to support video creation, such as for educational videos. At first glance, video creation seemed simpler than live-streaming since it doesn’t require real-time interaction, making it easier to control the output.\n
We received requests from customers, such as schools, who wanted to create personalized avatars and voices for their teachers—potentially dozens or even hundreds of unique profiles. Our marketing team was eager to prioritize this video creation feature, and the product manager also thought it would be easier to develop.\n
However, after discussing with the engineering team, especially the digital human rendering ML engineers, I realized that creating highly personalized avatars and voices at scale was technically challenging and resource-intensive. On the other hand, live-streaming functionality could start with a few high-quality, pre-designed avatars, making it faster to implement and more broadly appealing to customers.\n
I organized a meeting with the marketing, product, and engineering teams to share the technical constraints and discuss the potential workload. I also presented data showing the broader market potential for live-streaming features compared to the niche demand for highly customized avatars. After thorough discussion, we aligned on prioritizing live-streaming features while planning to support avatar customization in the next phase.\n
This approach ensured that we delivered impactful features quickly while addressing stakeholder concerns and setting realistic expectations. It also strengthened cross-functional collaboration and trust.""")

    with st.expander("What areas do you seek for growth? "):
        st.write("""I'm always seeking opportunities to grow both :blue-background[technically and as a leader].\n
On the leadership side, I want to further enhance my ability to coach and mentor engineers, helping them reach their full potential. While I have experience managing teams, I'm particularly focused on refining my skills in aligning individual goals with broader company objectives and fostering a collaborative environment that drives innovation.\n
Technically, I'm especially excited about advancing my expertise in Large Language Models (LLMs). With the rapid developments in this field, I see significant potential in pushing the boundaries of LLMs, particularly in fine-tuning them for specific tasks, improving the efficiency of model training and inference, and exploring how LLMs can be leveraged to build intelligent systems that better understand context, reason with data, and generate human-like responses.\n
Additionally, I'm focused on improving my communication with non-technical stakeholders to ensure that the business impact of ML projects is clear and aligns with the company's strategic objectives.""")

    with st.expander("Describe your failure. How did you conquer it? (Missed deadline for government project.)"):
        st.write("""One significant failure I encountered was during a project at CloudWalk for a government client, where we needed to develop a new feature for our knowledge engine to extract information from policy documents. We initially based our planning on sample documents provided, but the actual documents proved to be much more complex. They included a variety of formats, such as handwritten scans, which made accurate understanding and processing challenging.\n
I underestimated the complexity of integrating this new feature with our existing systems. Consequently, we missed our launch deadline, which affected the team’s morale and delayed other projects.\n
To address the issue, I led a thorough reassessment of the project requirements and identified gaps in our initial planning. We revised our approach by enhancing our model training processes to accommodate the diverse document formats and placing greater emphasis on risk management and regular progress reviews.\n
Ultimately, we successfully delivered the feature with a revised timeline, and it was well-received by the client. This experience highlighted the importance of thorough initial assessments and proactive risk management, and reinforced the need for flexibility and frequent updates in project planning to achieve successful outcomes.""")

    with st.expander("Describe a mistake you made during the live-stream product."):
        st.write("""1. Underestimating Technical Challenges\n
Mistake:\n
When initially planning the digital human project, I underestimated the complexity of integrating real-time rendering with the live-streaming platform. We ran into unexpected delays because the infrastructure couldn’t handle the computational load efficiently.\n
Lesson Learned:\n
This taught me the importance of investing more time in feasibility studies and technical prototyping before committing to a timeline. In future projects, I ensured a dedicated research phase to identify potential bottlenecks early.\n
2. Overloading the Team with Features\n
Mistake:\n
To make the product stand out, I initially pushed for multiple advanced features, like dynamic script generation and real-time Q&A, to be developed simultaneously. This stretched the team too hard and led to burnout.\n
Lesson Learned:\n
I realized the importance of prioritizing features based on impact and feasibility. I adopted a phased approach to development, focusing on delivering core functionality first and introducing advanced features incrementally.\n
3. Focusing Too Much on Technology, Not Enough on the User Experience\n
Mistake:\n
At the start of the digital human live-streaming project, we didn’t have a dedicated UX designer on the team. Instead, we relied on a highly skilled intern who was working part-time as our UX designer. She did an excellent job initially, but due to academic pressures, she had to leave and return to school earlier than expected.\n
Without a UX designer, we continued focusing heavily on the technical aspects, like improving rendering quality and optimizing live-streaming performance, but the user interface and experience didn’t receive the attention it needed. By the time we managed to hire a full-time UX designer, it became clear that the product’s interface didn’t meet user expectations. We ended up spending significant time and resources reworking the design, which delayed the overall project timeline.\n
Lesson Learned:\n
This experience taught me the importance of balancing technical development with user experience from the very beginning. I realized that neglecting UX could undermine the success of even the most technically advanced product.\n
Action Taken:\n
After this, I made it a priority to involve UX expertise early in every project. I also ensured we had a robust plan for resource continuity, so we wouldn’t face similar gaps in critical roles. Additionally, I started emphasizing the importance of user feedback loops during development, so we could identify and address usability issues sooner rather than later.\n
This shift not only improved the user experience but also helped us align better with user needs, leading to a more polished and successful product.""")

    with st.expander("What's your weakness?"):
        st.write("""One area where I’ve historically been less experienced is actively promoting a product to the public or directly advertising it. While I’m confident in communicating with internal stakeholders and business-side teams, my exposure to public-facing marketing and consumer outreach has been more limited.\n  
However, I’ve taken steps to address this. For instance, during my time at CloudWalk working on the digital human product, I collaborated closely with the marketing team to better understand how to position the product for consumers. I also participated in client-facing presentations to gather feedback and refine the product's messaging based on their needs. These experiences helped me build a stronger connection between product development and market expectations.\n  
I’m eager to grow further in this area by learning from experts in marketing and public relations, leveraging data-driven insights to shape consumer messaging, and participating more directly in public-facing engagements. I view this as an opportunity to enhance my ability to connect technical solutions with broader market impact.""")

    with st.expander("Describe a situation where you adapted to change / have to pivot during development."):
        st.write("""I adapt to change by staying :blue-background[flexible and open-minded], while focusing on continuous learning and maintaining clear communication. In dynamic environments, I actively seek to understand the reasons behind the change and quickly adjust my priorities accordingly.\n
For example, when our company shifted its strategy to focus more on large language model (LLM) applications after the release of ChatGPT, I conducted thorough research to understand the new landscape and identified a market opportunity in digital human technology. Despite this being a major change in direction, I successfully led the development of a new product that became a core offering and generated significant revenue for the company.\n
I’ve learned that the key to adapting well is staying proactive, communicating regularly with stakeholders, and ensuring that I align my actions with the evolving business goals. By staying resilient and open to feedback, I’m able to turn changes into opportunities for growth and innovation.""")

    with st.expander("Another example about adapting to change.(Prioritize audience interaction.)"):
        st.write("""**Situation:**  
Sure! While working on the digital human live-streaming product, we started out focusing on things like **enhancing script generation** and creating **high-quality virtual hosts**. But as we got more user feedback, it became clear that the real game-changer wasn’t just the hosts or the scripts—it was the ability to provide **real-time, automatic interaction with the audience** during live streams. Users told us that **timely and engaging responses** to audience questions were absolutely critical for live-streaming success.  

**Task:**  
Our challenge was to prioritize this audience interaction feature and make it stand out from competitors, who relied on manual FAQ setups for audience responses.  

**Action:**  
To tackle this, I worked closely with the product manager and engineering teams to **reprioritize our roadmap**. We made the development of the audience interaction module our **top priority**, pushing back less critical features to free up resources.  

Instead of going the manual FAQ route, we aimed for something more innovative:  
- We developed a **Retrieval Augmented Generation (RAG) system** that could extract answers directly from user-uploaded files and generate **real-time responses** automatically.  
- This required a lot of **fine-tuning of the LLM** and significant collaboration between the **machine learning team and infrastructure engineers** to handle the technical challenges.  

I also reallocated resources, assigning additional engineers to this module and adjusting deadlines to make sure we could deliver it without compromising quality.  

**Result:**  
The final feature combined **automated responses** with the option for **manual adjustments**, giving users a **flexible and powerful tool** to engage their audiences. It became a **key differentiator** for our product, setting us apart from competitors. After the release, we saw a big jump in **user satisfaction** and **adoption rates**.  

**Reflection:**  
This experience really reinforced the importance of staying **user-focused** and being **agile in a competitive market**. By listening to user feedback and addressing their most critical pain points, we didn’t just meet their needs—we delivered a feature that strengthened our product’s position in the market.""")

    with st.expander("Some other examples of adapting to change."):
        st.write("""Here are additional ideas:\n
---
#### **Example 1: Refactoring for Efficiency During Digital Human Development**\n  
During the early development of our digital human platform, we initially relied on an existing resources scheduling system for rendering, but it caused inefficiencies and frequent errors. Recognizing this as a blocker, I made the decision to pivot and lead the team in refactoring the system specifically for digital avatar rendering. This decision, though disruptive, improved efficiency by 5x and resolved the technical challenges, enabling us to deliver a stable product on time.\n
---
#### **Example 2: Shifting Focus from 3D to 2D Avatars**  \n
While working on the digital human product, there was internal debate about focusing on 2D vs. 3D avatars. Market feedback indicated that customers preferred cost-effective and easily customizable 2D avatars. Despite significant initial investment in 3D, I persuaded the team and stakeholders to pivot toward 2D. This shift aligned with user demand, and the resulting product exceeded revenue expectations with over 10,000 paying users.\n
---
#### **Example 3: Adjusting Timeline to Accommodate Large Model Integration**  \n
In one project, the product manager prioritized integrating a large language model as a key feature, but the engineering team found it challenging to achieve within the timeline. To adapt, I proposed a phased approach: starting with a simpler implementation of smaller models while reserving time for gradual large model integration. This compromise enabled us to meet immediate market needs without sacrificing long-term goals.\n
---
#### **Example 4: Adapting Strategy for Knowledge Engine Development**  \n
In our knowledge engine project, initially designed for structured datasets, we faced challenges with semi-structured web tables. Realizing the limitations, I led the team to pivot by incorporating machine learning-based visual recognition techniques. This adaptation allowed us to extract tables more effectively, expanding the scope of the project and delivering greater value to users.\n
---
#### **Example 5: Responding to Rapid Team Growth**  \n
When our team grew from 20 to over 30 people, it became clear that my hands-on management style was no longer scalable. I adapted by delegating more responsibilities, mentoring an architect to take on leadership for the digital human product, and establishing clear processes for cross-team communication. This pivot ensured the team maintained high productivity despite the rapid growth.\n
---
Each example demonstrates adaptability, critical decision-making, and a focus on aligning with business needs or solving critical challenges.""")

    with st.expander("What was some difficult feedback that you received? and why was it hard to receive?(Micro management)"):
        st.write("""One of the most difficult pieces of feedback I received was when I was promoted to engineering manager for the first time at Google. A colleague pointed out that I wasn’t giving enough autonomy to my team. I tended to get too involved in the details, especially when we were under tight deadlines. At the time, I thought I was helping, but the team felt micromanaged and less empowered to make decisions.\n
This feedback was hard to accept because I saw myself as a supportive leader, and it challenged my perception of my leadership style. Initially, I felt defensive, as I believed I was just ensuring everything was done right. But after reflecting on it, I realized that by not fully trusting my team, I was limiting their ability to grow and contributing to inefficiencies.\n
To address this, I began delegating more responsibility, trusting my team to handle challenges on their own, and stepping in only when necessary. Over time, this approach led to improved team morale, better decision-making, and allowed me to focus on higher-level strategic tasks. It was a tough lesson, but it made me a stronger and more effective leader.""")

    with st.expander("What was some difficult feedback that you received? **Another example** (Push the team too hard.)"):
        st.write("""**Answer:**  

**Situation:**  
Yeah, I can think of a time when we were working on the digital human live-streaming product. The pressure was intense—competition in the market was tough, and our team was a mix of people transitioning from B2B projects and new hires. The workload was heavy, and deadlines were tight. At one point, I got feedback that I was **pushing the team too hard** and setting expectations too high.  

**Task:**  
It was tough feedback to hear because the product was at a critical stage, and I felt we needed to push hard to meet our goals. But I realized that if the team was feeling burned out and uncertain, we wouldn’t be able to sustain our momentum. My task was to find a way to balance the urgency of the project with the team’s well-being.  

**Action:**  
I took the feedback seriously and made several changes:  
- **One-on-one meetings:** I sat down with each team member to understand their concerns and identify common themes.  
- **Competitive analysis:** I worked with the product manager to analyze how we compared to competitors—highlighting areas where we were ahead, where we were catching up, and what made us unique. This helped provide **context and reassurance** to the team.  
- **Phased goals:** We set clear, phased goals for the next three months, six months, and beyond. This broke the work into **manageable chunks** and gave the team a better sense of direction.  
- **Adjusting workloads:** I rebalanced individual tasks to make them more achievable without sacrificing quality.  
- **Advocating for resources:** I went to senior management and successfully secured additional resources to help ease the team’s burden.  

**Result:**  
These changes made a big difference. The team had a clearer understanding of our goals and how their work fit into the bigger picture. Workloads became more balanced—still challenging but manageable—and morale improved. Ultimately, we were able to **stay on track, meet our deadlines**, and keep the team motivated through a critical phase of the project.  

**Reflection:**  
This feedback was hard to hear because I knew we were at a make-or-break point for the product. But it taught me a lot about the importance of addressing concerns proactively, **communicating a clear vision**, and finding the right balance between urgency and sustainability. It was a valuable lesson in leadership.""")

    with st.expander("Tell me about a time you had to make a unpopular/tough decision.(Delay the LLM launch.)"):
        st.write("""When we launched the first version of our digital human product at CloudWalk, large language models were experiencing tremendous popularity. However, the initial version of our product didn’t have the model performance we wanted—it wasn’t delivering the level of quality and accuracy that our users would expect.\n
I made the unpopular decision to delay the launch of the product until we had improved the model’s performance. Instead of pushing out the unrefined version that was ready, I decided to hold off and use the additional time to fine-tune the model for better results. This wasn’t an easy choice, as the product team, sales, and other stakeholders were eager to release something in response to the high demand for large language models at that time.\n
I took the time to explain the situation to both the product manager and the sales team. I emphasized that releasing a suboptimal product could damage our brand’s reputation and lead to negative user experiences, which would ultimately hurt us more in the long run. I assured them that the additional time spent refining the model would pay off with better quality and user satisfaction.\n
At the same time, I worked closely with the machine learning team, prioritizing resources and closely managing the process to ensure we could improve the model quickly. We focused on fine-tuning and testing to achieve better performance.\n
Though this decision was unpopular, especially with the pressure to capitalize on the hype around large language models, it proved to be the right call. When we finally launched the improved version, the product was much better received by users, and it helped establish our product as a high-quality offering in the market.""")

    with st.expander("Another example of unpopular/tough decision.(Rejected B2b request.)"):
        st.write("""**Answer:**  

**Situation:**  
While working on the digital human product at CloudWalk, we faced a tough decision. A traditional B2B client approached us, asking for a customized version of our product. They wanted us to integrate their own live-streaming platform and add unique features, like deep support for some of their platform’s specialized live-streaming functions. The project promised quick revenue, but it would have required a lot of engineering resources and delayed the launch of our main product. On top of that, the custom features didn’t align with our long-term vision or market strategy.  

**Task:**  
I had to decide whether to take on this project for short-term gains or stay focused on finishing and launching our core product on time.  

**Action:**  
I made the tough call to **reject the B2B request** and prioritize our main product. It wasn’t a popular decision at first. The marketing team and senior management were worried about missing out on guaranteed money. To address their concerns, I explained why focusing on our core product was the better choice:

 - Integrating with the client’s live-streaming platform would have added significant complexity and risk to our development timeline.
 - Our core product had much greater potential for scalability and long-term success.
 - Delaying the launch would weaken our position in the competitive market.

**Result:**  
In the end, the decision paid off. We launched the product on time, gained over **10,000 paying users**, and generated **tens of millions in annual revenue**. That was far more than what the custom project would’ve brought in. It was a tough choice, but it helped us solidify our position as a market leader and set us up for long-term success.  

**Reflection:**  
This experience taught me that sometimes you have to make hard calls and stick to your vision, even if it’s not the easiest or most popular choice at the moment.""")

    st.header("Cross functional collaboration")
    with st.expander("Describe a time when you successfully partnered with a cross-functional team. What made it successful?"):
        st.write("""One of the most successful cross-functional collaborations I led was during the development of the digital human live-streaming product at CloudWalk. This project aimed to address the pain points in the e-commerce live-streaming industry by creating a scalable, cost-effective solution for personalized virtual hosts.\n
**Situation**:\n
My team, consisting of machine learning engineers and full-stack engineers, was responsible for the core platform development. However, the project required collaboration with digital human rendering ML engineers, infrastructure teams, as well as design, product, and marketing teams to ensure a seamless product experience and a successful market launch. Each team had distinct goals and priorities, making alignment crucial.\n
**Task**:\n
As the leader of the product, my role was to lead engineering efforts while ensuring alignment with the broader product vision. The challenge was to deliver a high-quality product within a tight deadline, despite competing priorities and the technical complexity of integrating multiple components, including ML models, rendering pipelines, and user-facing features.\n
**Action**:\n
To ensure success, I took several key steps:\n
1. Establishing a shared vision: I initiated a kickoff meeting with all stakeholders to define the product goals, success metrics, and key deliverables. This helped align everyone on the “why” behind the project.\n
2. Creating a collaborative roadmap: I worked with product managers to create a unified roadmap that outlined milestones and dependencies. Each team understood how their contributions fit into the larger picture.\n
3. Facilitating regular communication: I organized weekly cross-functional syncs to discuss progress, surface blockers, and address concerns. For example, when the rendering ML team faced challenges in achieving real-time performance, I connected them with infrastructure engineers to optimize GPU utilization.\n
4. Promoting transparency: I implemented tools like Jira to track progress, ensuring all teams had visibility into tasks and dependencies. This reduced miscommunication and improved accountability.\n
5. Fostering trust and collaboration: I encouraged open feedback and celebrated milestones. For example, when the design team created a prototype that received positive feedback during user testing, I ensured their work was recognized across teams.\n
**Result**:\n
The collaboration was a great success. We delivered the digital human live-streaming product on time and within budget. The product attracted over 10,000 paying users in its first year, generating tens of millions in revenue. It became a strategic asset for the company and significantly strengthened our market position.""")

    with st.expander("Tell me about a situation where you had to influence stakeholders with competing priorities. How did you handle it? (Prioritize LLM finetuning.)"):
        st.write("""**Situation**:\n
During the development of our digital human live-streaming product, we needed to fine-tune our in-house foundation large language model (LLM) to generate live-stream scripts and support real-time audience interaction. However, the foundation LLM team had limited experience with live-streaming data, and their roadmap was already packed with other high-priority tasks.\n
**Task**:\n
My goal was to influence the foundation LLM team to prioritize our project, collaborate closely with us, and ensure the LLM could meet the requirements for live-streaming script generation and real-time interaction.\n
**Action**:\n
To address this challenge, I adopted a collaborative and mutually beneficial approach:\n
1. Identifying shared value:\n
  - I emphasized that our digital human project was highly visible and a strategic priority for senior management. By contributing to its success, the foundation LLM team would gain significant visibility and credit for their work.\n
2. Proposing a win-win solution:\n
  - I suggested that my team could help to handle the live-stream data preparation, including data crawling and cleaning, which was a key blocker for them. This allowed them to focus on training the LLM.\n
3. Building trust and alignment:\n
  - I regularly communicated with the foundation LLM team to share progress, challenges, and updates on the product’s success. I also showcased how their improvements to the LLM directly impacted the product’s performance and user experience.\n
4. Demonstrating impact:\n
  - I shared early results from our collaboration, such as improved script generation quality and enhanced real-time interaction capabilities. These results reinforced the importance of their contributions and motivated them to stay engaged.\n
**Result**:\n
Through close collaboration, we successfully fine-tuned the foundation LLM to meet our needs. The script generation quality and real-time interaction capabilities improved significantly, helping our digital human product achieve its desired outcomes. The foundation LLM team gained recognition from senior management for their contributions, and our partnership strengthened.\n
This experience taught me the value of creating win-win solutions and aligning priorities to influence stakeholders effectively, even in the face of competing demands.""")

    with st.expander("A senior leader from a different org has challenged your approach to a specific problem your team is working on, in a weekly standup. What would you do next?"):
        st.write("""When a senior leader from a different org challenges my approach, I see it as an opportunity to refine our solution and align with broader organizational goals. Here's how I would handle it:\n
Listen and Understand:\n
I would start by actively listening to their perspective without being defensive. I’d ask clarifying questions to fully understand their concerns, whether it’s about technical feasibility, resource allocation, or alignment with company priorities. For example, I might ask, ‘Can you share more about why you think this approach might not work?’ or ‘What specific outcomes are you concerned about?’\n
Assess and Reflect:\n
After the meeting, I’d evaluate their feedback objectively. I’d discuss it with my team to identify whether there’s merit to their concerns or if it’s based on incomplete information. For instance, in our digital human live-streaming project, when an external stakeholder challenged our decision to prioritize live-streaming features over video creation, I reviewed their concerns with my team and revisited our cost-benefit analysis to ensure our approach was sound.\n
Engage in Dialogue:\n
If the challenge reveals gaps or misalignment, I’d schedule a follow-up discussion with the senior leader. I’d present data, rationale, and trade-offs behind our approach while being open to alternative solutions. If needed, I’d involve other stakeholders to ensure a balanced discussion. For example, I might bring in our product manager or ML engineers to explain technical details or user impact.\n
Collaborate on Adjustments (If Needed):\n
If the feedback leads to valid concerns, I’d work with my team to adjust our approach. For instance, in the live-streaming project, we adjusted our roadmap to incorporate additional feedback from stakeholders without losing sight of our priorities.\n
Communicate Clearly:\n
Finally, I’d ensure alignment by summarizing the outcome of the discussions and next steps to all stakeholders. This helps avoid misunderstandings and reinforces trust.\n
Throughout the process, my focus is on maintaining a collaborative mindset, aligning with organizational goals, and ensuring the best possible outcome for the project. Disagreements are inevitable in cross-functional work, but I believe they can lead to stronger solutions when approached constructively.""")

    with st.expander("How do you balance engineering limitations with customer requirements?"):
        st.write("""Balancing engineering limitations with customer requirements is critical to ensuring technical feasibility while meeting user needs. Here are the four key aspects of my approach:  \n
1. **Understanding Customer Goals**:  \n
   I start by clarifying not just what the customer is asking for but why it’s important. This helps uncover the underlying business goals and explore alternative solutions. For instance, when users complained about slow rendering speeds for our digital human product, I identified that the main frustration was uncertainty about completion times, not just the speed itself.\n  
2. **Evaluating Feasibility and Communicating Transparently**:  \n
   I assess the technical challenges and share clear updates with customers and stakeholders. In the rendering example, I proposed splitting videos into smaller segments for parallel processing and adding features like progress bars and notifications, which improved both performance and user satisfaction without overloading the engineering team.\n  
3. **Aligning Requests with Priorities**:  \n
   I align customer requests with our engineering roadmap by evaluating their impact and urgency. I prioritize high-value improvements while negotiating realistic timelines for more resource-intensive changes, ensuring steady progress without compromising team efficiency.\n  
4. **Delivering Incremental Value**:  \n
   I focus on phased delivery, rolling out immediate enhancements to address key pain points while planning longer-term optimizations. This ensures customers see quick improvements and stay engaged as we refine the solution.\n  
By combining open communication, creative problem-solving, and thoughtful prioritization, I balance technical constraints with delivering meaningful customer outcomes.  """)

    with st.expander("Explaining engineering concept to non-technical team members."):
        st.write("""Explaining engineering concepts to non-technical team members is a critical skill that I've practiced throughout my career. My approach revolves around several key principles:\n
1. Assess the audience: I always start by understanding my audience's background and existing knowledge. This helps me tailor my explanation appropriately.\n
2. Use simple language: I avoid technical jargon and use everyday terms whenever possible.\n
3. Employ analogies and real-world examples: These help bridge the gap between abstract concepts and familiar ideas.\n
4. Utilize visual aids: Diagrams, charts, or even simple sketches can often convey complex ideas more effectively than words alone.\n
5. Break down complex ideas: I divide intricate concepts into smaller, more manageable parts.\n
Let me give you a couple of examples:\n
Example 1: Explaining Neural Networks\n
If I needed to explain neural networks to a marketing team, I might say: 'Think of a neural network as a complex web of interconnected lights, where each light can be turned on or off based on certain inputs. Each light represents a 'neuron' that processes information. When we input data—like images or text—each light interacts with the others, turning on or off in response to patterns it recognizes. Just like how our brain learns from experiences, a neural network learns from a vast amount of data, adjusting the brightness of each light to improve its understanding over time. By the end of this process, the network becomes adept at making predictions or classifications based on new inputs.'\n
Example 2: Explaining the Concept of Model Training and Testing\n
To explain the concept of model training and testing to a product manager, I might use this analogy: 'Imagine training for a marathon. At first, you don't just run the full distance; instead, you practice in shorter segments to build your endurance and skills. During the training phase, you might track your time and distance to see how you improve. Once you feel ready, you participate in a test run, which is like model testing. Here, you evaluate your performance under real conditions to see if you can sustain your pace over the entire marathon distance. Similarly, in machine learning, we train our models on a dataset, refining their accuracy, and then we test them on new data to ensure they perform well in real-world scenarios.'""")

    with st.expander("How do you drive alignment when you're planning a project involving work across multiple teams?"):
        st.write("""When planning a project that involves multiple teams, my priority is to ensure alignment from the start by engaging with all key stakeholders early on. I start by identifying everyone who will be involved or impacted—whether they are product managers, designers, engineers, or other cross-functional teams. I set up individual 1:1 meetings with each stakeholder to share the project's vision and gather feedback.\n
During these one-on-one meetings, I make sure to understand each stakeholder's goals and how the project aligns with their priorities. I believe these discussions are crucial not only for gaining buy-in but also for identifying potential challenges or conflicts early. For instance, while I was at CloudWalk Technology, I managed the Knowledge Engine project alongside the digital human platform. We needed to support various B2B and government clients, and our digital human also required the knowledge engine to facilitate interactions with the audience. Each team had different priorities, so these conversations helped us find a middle ground while making necessary adjustments based on their feedback. This collaborative approach ensured that the project felt like a collective effort rather than a top-down initiative.\n
If I encounter resistance or differing opinions, I focus on understanding their concerns and explaining the broader vision, showing how the project will benefit everyone involved. These conversations help bridge any gaps in understanding and clarify any misalignments before they become bigger issues.\n
Once I have a strong sense of alignment, I create a comprehensive plan that outlines the project scope, vision, key metrics, and timelines. I ensure that the plan considers team dependencies—like having product and design take the lead initially, then transitioning to engineering, and finally looping in marketing or sales toward completion. This clear roadmap helps everyone understand their role and how it fits into the larger picture.\n
Throughout the project, I continue regular check-ins to make sure all teams remain aligned and address any issues that arise. The goal is to maintain a cohesive, collaborative environment while keeping the project moving forward efficiently.""")

    with st.expander("How do you ensure clear communication and alignment across your team, especially when working remotely or with distributed teams?"):
        st.write("""I have extensive experience working with remote and distributed teams. At Google, I worked remotely for almost two years during the pandemic, and at CloudWalk, I led a sub-team based in another city in China.\n  
To ensure clear communication and alignment, I focus on the following:  \n
1. Set Clear Goals and Expectations: I define priorities and timelines upfront, so everyone understands how their work contributes to the bigger picture.\n  
2. Leverage Collaboration Tools: Tools like Slack, Zoom, and Jira help maintain visibility and facilitate communication. For example, I used a shared task board to track progress and dependencies.\n  
3. Hold Regular Syncs: I conduct daily stand-ups or weekly updates to keep everyone aligned and quickly address blockers.  \n
4. Encourage Open Communication: I create a culture where team members feel comfortable sharing concerns and asking questions, supplemented by detailed documentation to avoid misunderstandings.\n  
5. Build Personal Connections: I organize virtual team-building activities to strengthen bonds and maintain morale.  \n
These strategies have enabled me to lead teams effectively, even when working across different locations and time zones.""")

    st.header("People management")
    with st.expander("Can you talk about how and why you become a people manager?"):
        st.write("""1. Start with the “Why” – Your Motivation\n
I became a people manager because I realized that my passion goes beyond just solving technical problems—I also enjoy helping others grow and succeed. Early in my career, I found myself naturally stepping into leadership roles, mentoring junior engineers, and facilitating collaboration within the team. I saw firsthand how impactful it can be to create an environment where people feel supported, motivated, and aligned toward a common goal. That inspired me to take the next step into formal management.\n
2. Transition to the “How” – Your Journey\n
My transition to management happened gradually. At Google, where I was a tech lead, I was already responsible for guiding technical direction and mentoring team members. I enjoyed the leadership aspect so much that I expressed interest in becoming a tech lead manager (TLM). My manager supported me, and I started managing a small team while staying hands-on with the technical work. This gave me a chance to learn the fundamentals of people management—like giving feedback, setting goals, and handling team dynamics—while still leveraging my technical expertise.\n
Later, at CloudWalk, I took on a larger leadership role as the team grew. I led cross-functional teams working on innovative projects like the digital human live-streaming platform. This required not just technical leadership but also fostering collaboration across engineering, product, and design, and managing diverse personalities and skill sets.\n
3. Reflect on the Impact\n
Becoming a people manager has been incredibly rewarding. It allows me to amplify my impact—not just by delivering great products but also by building high-performing teams and helping individuals achieve their potential. For example, I’ve been able to guide junior engineers to senior roles, resolve conflicts, and create a culture of learning and innovation within the team.\n
4. Connect to the Role/Company\n
I’m particularly excited about management roles at companies like Meta because they align with my belief in empowering teams to move fast, innovate, and make a meaningful impact. I thrive in environments where I can combine technical expertise with leadership to drive both team and business success.""")

    with st.expander("Describe a few of your peers at your company and the type of relationship you have with them"):
        st.write("""1. Start with Context\n
At my most recent company, I’ve developed relationships with a variety of peers across different roles, including mentors, colleagues at the same level, and key team members. These relationships fall into three main categories, each of which plays a critical role in my professional growth and the success of our projects.\n
2. Mentors or Coaches\n
The first category is mentors or coaches—people who guide me and provide valuable career advice. For example, when I was at CloudWalk, one of the co-founders acted as my mentor. They helped me navigate strategic decisions and offered insights into how to align technical innovation with business goals. Their guidance was instrumental in shaping my approach to leadership and product development.\n
3. Peers at My Level\n
The second category is peers who are my equals—my "battle partners." These are colleagues I’ve built trust with through collaboration, and we’ve achieved mutual success by working closely together. For instance, during my time at CloudWalk, I had a strong partnership with the leader of the infrastructure team and the foundation LLM team. Together, we solved critical challenges, such as optimizing LLM inference for real-time interaction and improving the foundation model for live-streaming use cases. These collaborations were built on mutual respect and shared ownership of outcomes.\n
4. Core Team Members\n
The third category is the core members of my own team. These are people I’ve worked with extensively, and we’ve built deep trust and understanding. I treat them not just as colleagues but as friends. For example, in the digital human project, I worked closely with a few key engineers and product managers. We helped each other during tough times, celebrated our successes together, and built a strong bond that kept everyone motivated.\n
5. Reflect on the Impact\n
These three types of relationships—mentors, peers, and team members—have been crucial to my success. My mentor helped me grow as a leader, my peers pushed me to achieve shared goals, and my team members created a collaborative environment where we could innovate and deliver impactful products.\n
6. Tie It Back to the Role\n
I believe that fostering these types of relationships is essential for success in any cross-functional environment, especially at Meta. Building trust, maintaining open communication, and supporting each other are key to driving innovation and delivering high-impact results.""")

    with st.expander("How do you identify talent gaps in your team, and how have you addressed them in the past?"):
        st.write("""**Situation**:\n
As a leader, I’ve always emphasized the importance of having a well-rounded team with complementary skills. During the development of our digital human live-streaming project, I noticed that while we had a strong core team of machine learning (ML) engineers and full-stack engineers, there was a noticeable gap in expertise related to digital human rendering and infrastructure, which was critical to the success of the project.\n
**Task**:\n
My task was to identify these talent gaps early on and address them effectively to ensure the project stayed on track and met its technical requirements.\n
**Action**:\n
1. Regular team assessments:\n
I regularly held one-on-one meetings with my team members to understand their strengths, weaknesses, and career goals. I also observed how they interacted with other teams and how their skills aligned with the project’s needs. This helped me identify specific gaps in expertise, particularly in areas like digital human rendering and infrastructure.\n
2. Collaboration with other teams:\n
I recognized that some gaps could be filled through collaboration with other teams. For example, we needed expertise in rendering, so I reached out to the digital human rendering team to establish a close collaboration. This helped bridge the gap without needing to hire immediately.\n
3. Hiring and training:\n
For gaps that couldn’t be filled through collaboration, I worked with HR to bring in external talent. In one case, we hired a senior infrastructure engineer to address the scalability challenges of our system. Additionally, I encouraged continuous learning within the team by providing resources for upskilling, such as online courses and internal knowledge-sharing sessions.\n
4. Mentorship and internal development:\n
I also mentored some of the team members who showed potential in areas where we had gaps. For example, one of my ML engineers had a strong foundation but lacked experience in real-time systems. I paired them with a more experienced engineer from the infrastructure team to accelerate their learning.\n
**Result**:\n
By identifying the talent gaps early and addressing them through a combination of collaboration, hiring, and internal development, we were able to build a more well-rounded team. The project’s success was a direct result of this effort, as we were able to improve the rendering quality and scalability of the system, which contributed to the product's market success.""")

    with st.expander("What strategies have you used to build a diverse and inclusive team?"):
        st.write("""Building a diverse and inclusive team has always been important to me because I believe diversity brings fresh perspectives, and inclusivity helps everyone do their best work. When I was assembling the team for our digital human live-streaming project—which included designers, product managers, front-end engineers, back-end engineers, and machine learning engineers—I made it a priority to create a group with a mix of skills, backgrounds, and experiences.\n
Here’s how I approached it:\n
1. Inclusive hiring practices:\n
  - I worked with HR to make sure our job descriptions were clear and appealing to a wide range of candidates, avoiding overly technical or exclusive language.\n
  - During interviews, I included diverse panel members to reduce bias and get different perspectives on each candidate.\n
  - I also focused on candidates with unique experiences, like those from non-traditional backgrounds, as long as they had the skills and potential to succeed.\n
2. Creating an inclusive environment:\n
  - From day one, I encouraged open communication and made sure everyone felt comfortable sharing their ideas. I also set up channels for anonymous feedback to address any concerns.\n
  - I regularly highlighted and celebrated team members’ contributions, ensuring everyone felt recognized.\n
  - We organized team-building activities, like “bubble tea time,” where team members shared aspects of their background, which helped us appreciate each other’s diversity.\n
3. Raising awareness:\n
  - I arranged workshops on topics like unconscious bias and inclusive leadership to help the team grow and understand these issues better.\n
  - I also encouraged mentorship, pairing senior engineers with junior team members, especially those from underrepresented groups, to support their growth.\n
4. Tracking progress:\n
  - I kept an eye on team diversity metrics and collected feedback to identify areas for improvement.\n
  - I set clear goals for diversity in hiring and promotions and made sure we discussed progress openly as a team.\n
The results were clear:\n
We built a team that was diverse in skills and backgrounds and inclusive in its culture. This diversity directly contributed to the success of our digital human project. For example, our designer brought fresh ideas that significantly improved the product’s user interface, making it more accessible to a wider audience. Overall, the team’s varied perspectives helped us solve problems creatively and deliver a better product.""")

    with st.expander("Share an example of a time when you fostered a culture of continuous learning within your team."):
        st.write("""When we were working on the digital human live-streaming product, many of our key features relied on large language models (LLMs), such as generating live-stream scripts and supporting real-time audience interaction. However, aside from our NLP machine learning engineer, most of the team didn’t have much experience with LLMs. To address this, I made it a priority to foster a culture of continuous learning.\n
Here’s what I did:\n
1. Organized internal learning sessions:\n
I set up regular team sessions where everyone could learn the basics of LLMs. These were collaborative, and team members from different roles shared their knowledge:\n
  - Machine learning engineers discussed the latest advancements in LLMs, focusing on the underlying principles.\n
  - Product managers shared insights on how other products in the market were innovating with LLM applications.\n
  - Infrastructure engineers talked about optimizing LLM inference efficiency.\n
2. Encouraged external learning:\n
I encouraged team members to attend external training programs and summits related to LLMs. Afterward, they would share what they learned with the rest of the team, so everyone could benefit.\n
3. Invited experts for in-house talks:\n
I arranged for colleagues from the foundation LLM team to give presentations on their latest developments and explain the underlying principles of their work. This helped bridge the gap between our teams and provided practical insights we could apply directly to our project.\n
The results were clear:\n
This culture of continuous learning not only helped our team improve their understanding of LLMs but also created a collaborative and innovative environment. For example, the infrastructure engineer’s optimizations significantly improved the efficiency of our LLM-based features, and the product manager’s insights inspired new ways to enhance our application. Overall, this learning culture empowered the team to tackle challenges more effectively and deliver a successful product.""")

    with st.expander("Tell me about a time when your team faced low morale. How did you address it?"):
        st.write("""Situation:\n
During the development of our digital human live-streaming product, my team was under significant pressure to deliver on tight deadlines. The workload was heavy, and several key features were technically challenging, which led to frustration and low morale. I also noticed that some engineers felt their hard work wasn’t being recognized, and they lacked a sense of accomplishment.\n
Task:\n
As the leader, I needed to lift the team’s morale, address their concerns, and ensure they stayed motivated to meet our goals.\n
Action:\n
1. Acknowledging the Issue: I first openly addressed the situation in a team meeting, letting everyone know that I recognized their hard work and understood their challenges.\n
2. Redistributing Workload: I worked with the product manager to reprioritize tasks and set more achievable short-term milestones. This helped reduce the immediate pressure.\n
3. Celebrating Wins: I introduced a weekly "Wins and Shoutouts" session where we celebrated even small achievements, such as solving a tough bug or completing a critical feature.\n
4. Encouraging Breaks: I encouraged team members to take short breaks and organized a team lunch to give everyone a chance to relax and bond.\n
5. Providing Support: I had one-on-one check-ins with each team member to understand their specific frustrations and offer support, whether it was helping with technical blockers or adjusting their workload.\n
6. Reassuring the Team: I reassured the team that we were progressing according to our plan. I explained that, while the beginning of any project is always the hardest, the experience we were gaining now would help us move more efficiently in the future.\n
Result:\n
These changes significantly boosted morale. The team felt their efforts were valued, and the recognition sessions created a more positive atmosphere. By breaking down the work into smaller, achievable goals, the team regained confidence. Ultimately, we delivered the project on time, and the positive energy carried forward into future projects.""")

    with st.expander("What is the structure of your 1:1s? How do you run 1:1s with your team?"):
        st.write("""I hold weekly 1:1s with my direct reports, and the structure is designed to keep things balanced between work-related updates, feedback, and personal development. Each 1:1 typically **starts with a personal check-in** to build rapport and understand how they’re feeling, both at work and outside of work. This helps create a comfortable space for open conversation.\n  
Next, **we talk about their current projects**. I ask about the progress they’ve made, any challenges they’re facing, and what kind of support they need from me to remove any blockers. I also provide feedback on their work and ask for their feedback on how I can improve as a manager. It’s important for me to foster an environment of open communication, so everyone feels comfortable sharing thoughts and concerns.\n  
In addition to project-related discussions, we **focus on their career goals**. I regularly check in on their growth and where they want to go in their careers. For example, I’ve helped several team members work toward promotions by guiding them on areas like priority management, communication strategies, and resource allocation. We’ll set short-term goals and discuss ways to improve in specific areas that align with their ambitions.\n  
I also make sure to **adapt the structure depending on the person’s needs**. For some, the focus might be more on technical challenges, while for others, it might be about leadership development. Finally, I always follow up with clear action items from our discussion, so there’s accountability and we can track progress over time. This helps ensure that everyone continues to grow and develop in their role.""")

    with st.expander("How does your 1:1 discussion change between ICs and managers?"):
        st.write("""**With Individual Contributors (ICs)**:\n
For ICs, I focus more on their day-to-day work, technical challenges, and growth opportunities.\n
- Project Updates and Roadblocks: I ask about their progress, blockers, and how I can support them—whether it’s unblocking dependencies, clarifying priorities, or providing resources.\n
- Skill Development: I explore opportunities to help them grow, such as mentoring, taking on stretch tasks, or attending training. For example, in our digital human project, I encouraged ICs to learn more about LLMs and even organized group learning sessions.\n
- Feedback and Recognition: I provide constructive feedback on their work and recognize their achievements to keep them motivated.\n
- Well-Being and Engagement: I check in on how they’re feeling about their workload, team dynamics, and overall morale to ensure they’re engaged and not overwhelmed.\n
**With Managers**:\n
For managers, the conversation shifts more toward team dynamics, leadership challenges, and broader strategic alignment.\n
- Team Health: I ask about team morale, any conflicts, or performance concerns, and help brainstorm ways to address these challenges.\n
- Delegation and Leadership: I encourage them to share how they’re empowering their team, delegating effectively, and developing their ICs.\n
- Strategic Alignment: I discuss how their team’s work aligns with overall goals and priorities, ensuring they’re focused on the most impactful work.\n
- Coaching and Growth: I provide guidance on their leadership skills, such as communication, decision-making, and stakeholder management. I also help them identify opportunities for their own growth, like taking on cross-functional projects or attending leadership training.""")

    with st.expander("How would you describe your role in coaching and career development?"):
        st.write("""As a coach, my primary goal is to empower team members to grow both personally and professionally by aligning their aspirations with meaningful opportunities. Here are the four most important aspects of my coaching approach:  \n
1. **Personalized Development Plans**:  \n
   I work closely with team members to understand their goals and strengths, creating tailored development plans that focus on skill enhancement and career progression.\n  
2. **Actionable Feedback**:  \n
   I provide regular, constructive feedback during 1:1s, ensuring it is specific and actionable to guide improvement in both technical and leadership areas.\n  
3. **Encouraging Leadership Through Challenges**:  \n
   I help team members step out of their comfort zones by assigning leadership roles or challenging projects. For example, I guided an architect to transition into an engineering manager role by providing mentorship and growth opportunities.\n  
4. **Fostering a Growth-Oriented Environment**:  \n
   I cultivate an environment where team members feel supported, are held accountable, and are empowered to reach their full potential.  """)

    with st.expander("Have you ever coached someone?"):
        st.write("""**Situation:**\n  
While I was working at Google, my skip-level manager mentioned a junior ML developer in a neighboring team who was struggling to transition their theoretical knowledge into practical applications. Recognizing their potential, I volunteered to coach them. In my understanding, the difference between mentoring and coaching is that mentoring is more about providing long-term career guidance and sharing experiences, while coaching is focused on helping someone develop specific skills or overcome immediate challenges.\n  
**Task:**  \n
My goal as their coach was to help them improve their ability to implement machine learning models in production, enhance their coding practices, and gain confidence in tackling real-world problems.\n  
**Action:**  \n
I started by meeting with the developer to understand their pain points and goals. Together, we outlined key areas for growth, such as:\n  
- **Model optimization:** Improving the performance of their ML models.  \n
- **Deployment:** Gaining hands-on experience with deployment pipelines.  \n
- **Coding practices:** Writing cleaner, more maintainable code.  \n
Here’s how I approached the coaching:  \n
- **One-on-one sessions:** We had regular meetings where I provided actionable feedback and reviewed their progress.\n  
- **Hands-on support:** I walked them through debugging and optimization techniques during pair programming sessions. \n 
- **Resource recommendations:** I shared curated learning materials, such as technical blogs and open-source projects, tailored to their needs.\n  
- **Project-based learning:** I guided them on completing a small end-to-end ML project, breaking it into manageable steps and celebrating milestones.\n  
**Result:**  \n
Within a few months, the developer showed remarkable improvement. They successfully deployed their first ML model to production, which not only boosted their confidence but also added value to their team. They became more proactive in seeking feedback and collaborating on cross-team projects. This growth also strengthened the collaboration between our teams, as they could take on more responsibilities independently.\n  
By stepping in as a coach, I helped this developer overcome their challenges and contribute more effectively, which ultimately benefited both their personal growth and the broader organization.""")

    with st.expander("Can you tell me about your leadership style?"):
        st.write("""My leadership style is flexible because I believe that different situations and team dynamics require different approaches. While I adapt my style based on the context, I primarily rely on a combination of visionary coaching and democratic leadership.\n
I’m a visionary leader in the sense that I set a clear vision for the team and inspire them by aligning their personal goals with the broader mission. Sometimes, I’m the only person who has the most comprehensive understanding of the full big picture, and I ensure that I communicate this effectively so everyone understands how their work contributes to the project’s overall success. This helps the team stay motivated and focused, especially when tackling complex challenges or when there is a long-term goal to achieve.\n
At the same time, I employ a democratic style, encouraging open communication, collaboration, and input from team members in decision-making. I value diverse perspectives and actively seek feedback from the team to ensure everyone feels heard and empowered. This not only promotes a sense of ownership and accountability but also leads to better ideas and stronger team cohesion.\n
For example, at the beginning of a project, I set a clear vision for the product we were building and communicated how each team member’s work was integral to our success. I also made it a point to involve the team in key decisions, whether it was architecture design or project prioritization. By blending these styles, we were able to work together efficiently while also fostering a collaborative, empowered environment.""")

    with st.expander("Which leadership style do you least prefer?"):
        st.write("""The leadership style I least prefer is autocratic[ɔːtəˈkrætɪk] leadership. While some leaders may not intentionally adopt an autocratic style, they can become unaware of it over time. They might believe they are making the best decisions, but in reality, they may be shutting down constructive feedback or refusing to delegate authority. This creates an environment where team members feel reluctant to offer opinions, and the leader ends up making all the decisions without input from the team.\n
This approach can stifle[ˈstaɪf(ə)l] creativity, reduce engagement, and ultimately limit the team’s potential. Over time, the leader may not even realize they’ve become autocratic because they don’t recognize the impact of their behavior.\n
I prefer to lead with a visionary and democratic style, where I set a clear vision for the team while encouraging open communication, collaboration, and shared decision-making. This empowers team members and ensures that everyone is involved, leading to more innovative solutions and a more motivated team.""")

    with st.expander("How would you go about building credibility with your reports?"):
        st.write("""Building credibility with my reports is a gradual process, and it starts with leading by example. I make sure to demonstrate reliability, competence, and a strong work ethic. When my team sees that I am committed to the same standards I expect from them, it helps establish mutual respect.\n
Open communication is another key factor. I aim to be transparent, approachable, and receptive to feedback. By creating an environment where people feel comfortable sharing their ideas and concerns, I build trust and make it clear that their input is valued.\n
I also focus on supporting and empowering my team. I give them the resources, autonomy, and guidance they need to succeed, and I trust them to take ownership of their projects. This not only fosters a sense of responsibility but also builds trust in my leadership.\n
One of the most important aspects of building credibility is to deliver on promises. I make sure to follow through on commitments and ensure that I hold myself accountable. When the team sees that I am reliable, it reinforces their trust in me as a leader.\n
Lastly, I show a genuine interest in their development. I take time to understand their career goals and offer guidance to help them grow. By investing in their growth, I demonstrate that I care about their success, which further strengthens the trust and credibility I have with them.""")

    st.header("Performance management")
    with st.expander("Tell me about a time you created a career development plan for a team member. (Architect to manager)"):
        st.write("""In my current role at CloudWalk, I lead a diverse engineering team working on the digital human live-streaming product. One of my priorities has been to understand each team member’s career aspirations and to work with them to create personalized development plans that align with both their goals and the needs of the organization.\n  
One specific example involved an architect on my team who had strong technical skills but expressed a desire to take on leadership responsibilities. During our one-on-one discussions, they shared their interest in transitioning into a management role, but they lacked prior experience in areas like team leadership and project coordination.  \n
To support their growth, I created a tailored career development plan. We focused on three key areas:  \n
1. **Leadership and management skills:** I provided mentorship on topics such as effective team communication, conflict resolution, and decision-making. We also discussed strategies for resource allocation and managing competing priorities.\n  
2. **Hands-on experience:** I gave them the responsibility of leading the engineering development for our digital human product. This included managing a team of engineers, coordinating with cross-functional stakeholders, and owning the delivery of key project milestones.\n  
3. **Continuous feedback and coaching:** I held regular check-ins to discuss their progress, provide constructive feedback, and address challenges. I also encouraged them to reflect on their experiences to identify areas for improvement.  \n
Over time, their confidence and skills as a leader grew significantly. They successfully transitioned into the role of an engineering manager, driving critical project milestones, building a high-performing team, and contributing to the product’s success.\n  
This experience reinforced the importance of creating clear and actionable development plans, providing opportunities for hands-on growth, and offering ongoing support. It’s rewarding to see team members achieve their career goals while also adding value to the organization.""")

    with st.expander("Another example of creating development plan for a team member.(Engineer to product manager)"):
        st.write("""In my role at CloudWalk, I focus on helping team members achieve their career goals by providing tailored development plans. Another example of this was with an engineer who expressed a strong interest in transitioning into product management. While they had great technical skills, they wanted to gain a deeper understanding of product strategy, customer needs, and market considerations.\n
To support their career transition, I developed a personalized plan that allowed them to gradually gain experience in product management while still contributing as an engineer. The first step was pairing them with our product manager for mentorship. They had the opportunity to shadow our product manager during meetings, which gave them exposure to how product decisions were made, how user feedback was incorporated, and how to prioritize features in a roadmap.\n  
As they became more comfortable, I gave them the opportunity to participate more actively in planning sessions, where they contributed ideas on feature development and learned how to balance technical constraints with user needs. This exposure helped them understand the broader context of product development.  \n
The next step was to give them full ownership of a feature. They were responsible for both the technical implementation and managing the product side, which included collaborating with the design team, gathering feedback from stakeholders, and tracking user metrics. This hands-on experience helped them gain confidence in balancing both engineering and product management responsibilities.\n  
Over time, they successfully transitioned into a hybrid role, taking on both engineering and product management responsibilities. They worked closely with the engineering team while also driving product decisions and collaborating with other departments. This experience allowed them to develop the skills and confidence needed to take on more leadership in product management, and they eventually became a key player in defining product strategy for future features.\n  
This experience showed me the importance of providing practical learning opportunities, mentorship, and real-world responsibility to help team members achieve their career goals. It was rewarding to see them grow into a hybrid role that utilized both their engineering background and new product management skills.""")

    with st.expander("What's your strategy to handle poor performers?"):
        st.write("""When handling a poor performer, my first step is to assess the situation to understand the root cause. Sometimes, performance issues can stem from unclear expectations, personal challenges, or a lack of resources. I try to understand whether it's a skill gap, a motivation issue, or something else entirely.\n
Once I have a clear understanding, I have an open and honest conversation with the individual. I aim to provide specific, actionable feedback, focusing on what’s not working and why, while also acknowledging their strengths. It's important to approach this conversation with empathy, so they feel supported rather than attacked.\n
Next, I work with them to set clear goals and provide any resources or support they may need to improve, whether it’s additional training, mentorship, or adjusting their workload. I emphasize that improvement is expected, but I also make sure they understand the steps they can take to succeed.\n
I monitor progress regularly and provide feedback along the way. I follow up to see if the individual is on track and make adjustments if necessary. This also gives the person a chance to ask questions or raise concerns.\n
If the individual still doesn't show improvement despite my efforts, I take tough decisions if needed. This could mean reassignment, role adjustments, or, in extreme cases, separation from the team. Ultimately, my goal is to ensure the success of both the individual and the team, and sometimes that means making difficult decisions for the greater good.""")

    with st.expander("Have you helped a low performer to improve? (Junior ML engineer)"):
        st.write("""Situation:\n
When we started working on the digital human project at CloudWalk, a junior machine learning developer joined our team after a reorganization. They had experience working on machine learning projects like fraud detection algorithms, but they didn’t have much experience with NLP, especially with large language models (LLMs). As a result, they struggled significantly in the beginning, particularly with understanding the complexities of LLMs and how to apply them to our project.\n
Task:\n
My task was to help this junior developer overcome their struggles, build their confidence in NLP and LLMs, and ensure they could contribute effectively to the project without falling behind.\n
Action:\n
1. Assessing the Knowledge Gap:\n
I first had a one-on-one meeting with the junior developer to understand where they were struggling and what specific aspects of NLP and LLMs they found challenging. It became clear that they needed a deeper understanding of how LLMs work and how to integrate them into the live-streaming use case we were developing.\n
2. Providing Resources and Support:\n
I connected them with a senior machine learning engineer on the team who had extensive experience in NLP and LLMs. I also provided them with learning resources such as online courses, research papers, and internal documentation that could help them get up to speed. Additionally, I encouraged them to pair up with the senior engineer for a few tasks to gain hands-on experience.\n
3. Breaking Down Tasks and Setting Milestones:\n
To prevent them from feeling overwhelmed, I assigned smaller, manageable tasks related to LLMs, gradually increasing in complexity as their understanding improved. We set clear milestones for each task, and I held regular check-ins to provide feedback, answer questions, and ensure they felt supported.\n
4. Fostering a Collaborative Environment:\n
I made sure to foster a collaborative team environment where they felt comfortable asking questions and sharing their progress. I also encouraged the entire team to provide constructive feedback and support to help them feel more integrated into the project.\n
Result:\n
After about three months, the junior developer’s confidence and performance improved significantly. They were able to contribute meaningfully to the project, particularly in fine-tuning the LLM for live-streaming script generation. Their understanding of NLP and LLMs grew, and they became a valuable asset to the team. By the end of the project, they had taken on more complex tasks and were able to work independently on key components of the system.""")

    with st.expander("Tell me about a time how you handled poor performer and improved the performance. (Backend engineer)"):
        st.write(""" When we transitioned from the knowledge engine project to the digital human live-streaming project, one of the backend engineers on my team, who had been a strong performer in the past, started struggling. Their code quality and delivery speed declined, and it became clear they were having difficulty adapting.\n
After discussing with them in one-on-one meetings, I discovered the root cause: while they were highly skilled in backend development for B2B projects, this was their first time working on a consumer-facing product. They lacked understanding of the live-streaming business logic, which was crucial to the new project.\n
To address this, I created a tailored improvement plan. I encouraged them to immerse themselves in the business by:\n
1. Watching live-streaming sessions to understand the industry and the role of hosts and audience interactions.\n
2. Participating in live-streaming sessions and shadowing the process to see how digital tools integrate into the ecosystem.\n
3. I paired them with a product manager and a more experienced engineer to explain the business requirements in detail and help them connect the dots between the product vision and backend implementation.\n
Over the next few months, their performance significantly improved. They became more confident in understanding the product requirements and started proactively contributing ideas for improving the backend systems. Their newfound business knowledge not only helped the project but also became a strength they could leverage in future consumer-facing projects.\n
This experience reinforced the importance of identifying the root cause of performance issues and addressing them through targeted development rather than making assumptions about capability.""")

    with st.expander("Describe a time you coached someone on improving their communication skills."):
        st.write("""During the development of our digital human live-streaming project, I noticed that one of our talented front-end engineers, who was instrumental in implementing key features, struggled to effectively communicate their ideas during cross-functional meetings. Their technical insights were valuable, but the way they presented often left non-technical stakeholders, like the designer and product manager, confused, which sometimes slowed decision-making.\n
Here’s how I approached it:\n
1. One-on-one feedback sessions:\n
I scheduled a private meeting to discuss the issue constructively. I highlighted their strengths and explained how improving communication could amplify their impact on the project.\n
2. Practical coaching:\n
I worked with them to structure their thoughts more clearly. For example, we practiced using the “What, Why, How” framework:\n
  - Start with what the problem or solution is.\n
  - Explain why it matters to the project or stakeholders.\n
  - Conclude with how it works or what steps need to be taken.\n
3. Setting clear expectations:\n
I received feedback from our product manager that during discussions, the engineer even showed the code, which made it hard for non-technical team members to follow. Based on this, I proposed a requirement: when engineers present their work, they must ensure that the designer and product manager can understand what they are talking about. This helped set a clear standard for communication.\n
4. Role-playing and preparation:\n
Before key meetings, I encouraged the engineer to rehearse their points with me or a peer. We role-played scenarios where they had to explain their ideas to non-technical stakeholders, focusing on using simpler language and analogies instead of diving directly into technical details like code.\n
5. Team-wide initiatives:\n
To foster better communication across the entire team, I introduced weekly team meetings where everyone took turns presenting their work. The key requirement was to ensure that all audience members, regardless of their role, could understand the presentation. This not only improved individual communication skills but also created a culture of clarity and inclusiveness.\n
The result:\n
Over time, the engineer’s communication improved significantly. They became more confident in presenting their ideas, and stakeholders engaged more positively with their contributions. One memorable moment was when they explained a complex machine-learning optimization to our product manager and designer using an analogy, which helped the team make a critical decision quickly.\n
This experience reinforced for me the importance of coaching team members not just on technical skills but also on soft skills like communication. It also highlighted the value of setting clear expectations and creating team-wide practices to encourage continuous improvement.""")

    with st.expander("Tell me about a time you manage someone out of the team, walk through the details. (Junior ML engineer)"):
        st.write("""Situation:\n
When we started working on the digital human project, our team underwent a reorganization, and a junior machine learning developer joined our team. This engineer had experience in facial recognition, but they lacked expertise in Natural Language Processing (NLP), particularly with large language models (LLMs), which were central to our project. Despite providing them with resources and guidance, they struggled to adapt to the NLP and LLM requirements of the project.\n
Task:\n
As the team lead, it was my responsibility to ensure the team was performing at a high level and meeting the expectations of the project. Given the importance of NLP and LLMs to the digital human project, I had to assess whether this engineer could develop the necessary skills in time or if their skill set was better suited to another role.\n
Action:\n
1. Initial Support and Development Plan:\n
Recognizing the engineer’s strengths in facial recognition, I created a development plan to help them bridge the gap in NLP and LLMs. I provided access to relevant learning resources, set up mentoring sessions with senior team members, and assigned tasks that leveraged their existing expertise while gradually introducing them to NLP-related tasks.\n
2. Ongoing Monitoring and Feedback:\n
Over the next few months, I closely monitored their progress and provided regular feedback. I encouraged them to collaborate with senior engineers on NLP tasks and to ask questions when needed. However, despite these efforts, their performance in NLP-related tasks remained below expectations.\n
3. Evaluating the Situation:\n
After several months of providing support and feedback, it became clear that the engineer was not making the necessary progress in mastering NLP and LLMs. I had to evaluate whether this role was a good fit for them. Given their expertise in facial recognition and liveness detection, I believed they could excel in a different role within the company that better aligned with their strengths.\n
4. Having a Difficult Conversation:\n
I scheduled a one-on-one meeting with the engineer to discuss their performance. I explained that despite the support and resources provided, they had not been able to meet the expectations for the role, particularly in NLP. I reassured them that this decision wasn’t a reflection of their overall abilities but rather a mismatch between their skill set and the specific demands of the project. I offered to help them transition to a different role within the company that would better align with their strengths.\n
5. Providing Transition Support:\n
I worked with HR to ensure a smooth transition for the engineer. I helped them identify potential opportunities within the company that were more aligned with their expertise in facial recognition and liveness detection. I provided feedback on areas they could work on to improve their future prospects and offered to be a reference for them as they explored new opportunities.\n
Result:\n
The engineer successfully found another role within the company that better matched their experience and skill set in facial recognition and liveness detection. The new role allowed them to leverage their existing strengths, and they were able to thrive in a position that didn’t require deep expertise in NLP. This outcome was beneficial for both the engineer and the team, as it ensured that the team could focus on the critical tasks of the digital human project while the engineer was in a role that was a better fit for their capabilities.""")

    with st.expander("Have you ever promoted anyone? Describe the process. (Google Junior engineer)"):
        st.write("""I've helped several team members get promoted, but one case that stands out is when I first became a manager at Google.I promoted a junior engineer to a senior engineer role. This engineer had already shown strong technical skills and a proactive approach to problem-solving, but to move to the senior role, they needed to develop more leadership qualities and take ownership of larger projects.\n
The process began by assessing their performance against the expectations for senior engineers, which included not only technical proficiency but also leadership in mentoring, involvement in high-impact projects, and making architectural decisions. After identifying their potential, I worked with them to create a development plan focusing on enhancing their technical leadership, getting deeper into system design, and mentoring junior team members.\n
I then assigned them more challenging tasks, such as leading the design and execution of a major project. I also encouraged them to present their ideas during team meetings, which helped them build confidence in stakeholder communication and justifying technical decisions. We had regular 1:1s to track progress, and I ensured they gained visibility across the team and other groups.\n
Once they consistently demonstrated leadership and technical depth, I advocated for their promotion, highlighting their growth in influence and responsibility. After their promotion to senior engineer, they took on even more critical projects and became a mentor to others, significantly contributing to the team's success.\n
This experience not only boosted their career but also strengthened the team by adding a strong technical leader.""")

    with st.expander("Tell me about a time how you handled performance bias in your team. (Quiet engineer)"):
        st.write("""Sure! Once, I noticed a quiet junior engineer on my team wasn’t getting much recognition during team discussions. They rarely spoke up, so some teammates unconsciously assumed they weren’t contributing as much. I realized this was a performance bias—where more vocal or visible team members were perceived as higher performers, even if quieter members were making equally important contributions.

The turning point for me was during a review of recent system improvements. I dug into the details and discovered that this engineer had fixed some critical bugs in our digital human rendering system. These fixes significantly improved the system's efficiency and reduced errors, but because their work happened behind the scenes, it wasn’t obvious to others.

To address this, I made it a priority to highlight their contributions in team meetings. I explained to the team how their bug fixes had improved our system’s stability and efficiency, emphasizing the value of their work. I also had a one-on-one with the engineer to encourage them to share updates more often. I realized they were hesitant because they weren’t confident their work was "worth mentioning," so I reassured them that every contribution mattered.

At the same time, I took steps to address the team’s overall mindset. I reminded everyone that impactful work doesn’t always look the same—some contributions are highly visible, like presenting ideas, while others are quieter but equally critical, like debugging or refining systems. I also encouraged a culture where team members actively ask quieter colleagues for their input during discussions.

Over time, the engineer became more comfortable sharing their work, and the team grew better at recognizing contributions from everyone, not just the most vocal members. This experience taught me to be more mindful of performance bias and to actively look beyond surface-level impressions to ensure everyone’s efforts are acknowledged and valued.""")

    with st.expander("Tell me about a time you had to gave some difficult feedback.(Teamwork issue)"):
        st.write("""
One time, I had to give tough feedback to an engineer on my team who was very talented but struggled with teamwork. They were used to working independently and often made decisions without involving others. This led to some friction in the team because others felt left out or had to redo work to align with the overall direction.

I sat down with them one-on-one and started by acknowledging their strengths, like their technical skills and ability to deliver results quickly. Then, I shared specific examples of where their approach had caused issues, like when they implemented a major change without consulting the team, which delayed the project timeline.

I made sure to focus on the impact of their actions, not their intentions. For example, I said, "I know you're trying to move fast and solve problems, which is great, but when decisions are made in isolation, it can slow the team down because we have to backtrack to align everything."

We discussed ways they could improve, like involving others earlier in the process, asking for feedback, and sharing updates regularly. I also offered to support them by checking in during team meetings to make sure everyone was on the same page.

It wasn’t easy because I knew they might feel criticized, but they appreciated the honesty and worked on improving. Over time, they became a much better team player, and the team dynamics improved significantly. 

The key was balancing honesty with empathy and framing the feedback as an opportunity for growth rather than a critique of their character.""")

    with st.expander("How do you handle low performance and communicate negative feedback"):
        st.write("""When addressing poor performance, I start by trying to understand the root cause. Whether it’s a lack of clarity on expectations, a skill gap, personal challenges, or motivation issues, I believe it's important to diagnose the situation first. I approach this with empathy, ensuring that I understand the person’s perspective.\n
Once the cause is clear, I schedule a private one-on-one meeting to give honest, constructive feedback. I focus on specific examples of where performance has been lacking, while ensuring I’m objective and not critical of the individual as a person. For example, instead of saying, ‘You’re not performing well,’ I’d say, ‘In the last project, the deadlines were missed due to X, and here’s how we can address that going forward.’\n
I also collaborate with the individual on a plan for improvement. We work together to identify areas for growth and set clear, achievable goals. I offer support such as additional resources, training, or even mentoring to help them improve in those areas.\n
After that, I make it a point to monitor progress regularly. During follow-up meetings, we discuss their progress, refine the plan if necessary, and I continue offering feedback and encouragement. If the performance improves, I make sure to acknowledge and celebrate those improvements, reinforcing positive behavior.\n
Throughout the process, I remain professional and empathetic[ˌempəˈθetɪk], because I understand that poor performance can often be stressful for the individual. My goal is to help them succeed, and I ensure they feel supported and motivated to improve rather than discouraged.""")

    with st.expander("How do you handle uneven performance when someone excels in some areas but struggles in others"):
        st.write("""When someone excels in certain areas but struggles in others, I take a balanced approach. For example, in a previous project, one of my team members was exceptional at technical problem-solving and had strong execution skills, but they struggled with collaboration and communication with cross-functional teams.\n
I first made sure to acknowledge and appreciate their technical expertise and how it contributed to the success of the project. It's important to reinforce their strengths and make sure they feel valued for what they do well. This creates a positive foundation for feedback on their weaker areas.\n
Then, we discussed the challenges in communication and collaboration. I worked with them to understand the root causes—whether it was a lack of confidence, understanding of the team dynamics, or something else. We co-created an action plan that included mentoring sessions, clear guidelines on collaboration, and specific goals such as leading more cross-functional meetings.\n
I also encouraged them to leverage their technical knowledge when communicating with others, as their expertise naturally earned respect from colleagues. Over time, with targeted feedback and support, they began to improve their communication skills, and their ability to work with cross-functional teams improved significantly.\n
Ultimately, by recognizing their strengths and providing structured support for their weaknesses, I was able to help them grow into a more well-rounded team member, which boosted their confidence and performance in all areas.""")

    with st.expander("How do you identify performance issues?"):
        st.write("""I believe identifying performance issues starts with setting clear expectations upfront. At the beginning of every project, I ensure that every team member knows exactly what is expected in terms of deliverables, quality, and deadlines. This clarity helps in assessing performance accurately.\n
Next, I regularly monitor progress through weekly check-ins, project updates, and direct observation. I also keep track of key performance indicators like deadlines, productivity, and the quality of work. If there are discrepancies between what was expected and the actual outcome, that’s a clear signal that there might be a performance issue.\n
In addition to data and metrics, I actively seek feedback from peers and cross-functional teams. Sometimes, team members working with the individual might have insights that I don’t directly see. I also keep an eye out for behavioral changes—such as disengagement, missed deadlines, or a drop in communication, which can indicate underlying issues.\n
Finally, when I do notice signs of a performance issue, I address it proactively. I have an open, honest conversation with the individual to understand the root cause, whether it’s lack of clarity, external challenges, or skill gaps. Together, we create an action plan to improve their performance, and I provide ongoing support and feedback to ensure they stay on track.""")

    with st.expander("Tell me about a time you had layoff communication."):
        st.write("""This is a particularly challenging task, and I’ve only had one experience with it. At CloudWalk, due to a strategic shift, we decided to focus more on our Digital Human Platform and reduce resources on our B2B and Government client business. Unfortunately, this meant that we had to make some tough decisions, including laying off a Technical Project Manager who had a strong track record in B2B projects.\n
When I communicated the layoff, I made sure to be transparent and direct about the reasons behind the decision, explaining that it was based on the evolving company strategy and not related to the individual’s performance. I also made it clear that this was a difficult decision for the company, as their contributions had been highly valued.\n
I approached the conversation with empathy and respect. I acknowledged the impact this would have on the individual’s career and expressed gratitude for their hard work. During the conversation, I offered support, including severance[ˈsevərəns] packages, access to career coaching, and job placement assistance. I wanted to ensure they felt supported during this transition, and we discussed their next steps and options in detail.\n
Afterward, I communicated with the rest of the team, being honest about the changes while focusing on how we could all contribute to the company’s new direction. I wanted to keep morale high and reassure everyone that we were committed to providing support as we navigated through these changes together.""")

    st.header("Project retrospective")
    with st.expander("Can you talk about a gap you identified during a project? How did you address it?"):
        st.write("""Situation:\n
During the development of our digital human live-streaming platform, we noticed a gap in how the system handled user interactions. Users often asked irrelevant or unproductive questions, like "Can you count from 1 to 1000?" These questions wasted computational resources and distracted the digital human from engaging in meaningful interactions, reducing the overall user experience.\n
Task:\n
Our goal was to address this issue by creating a system to filter out unproductive questions while maintaining a seamless user experience. This required building a robust classifier that could accurately distinguish between productive and unproductive queries.\n
Action:\n
To tackle this, we collaborated closely with the data annotation team to prepare a high-quality labeled dataset. This involved several steps:\n
- Data Collection: Crawling a large dataset of live-stream interactions.\n
- Data Preprocessing: Cleaning and organizing the data for annotation.\n
- Annotation Guidelines: Creating clear guidelines for annotators to differentiate productive from unproductive questions.\n
- Quality Monitoring: Regularly reviewing the annotated data to ensure high accuracy and providing timely feedback to the annotators.\n
Once the dataset was ready, we fine-tuned our model using this data. We also optimized the classification threshold to balance precision and recall, ensuring minimal false positives or negatives. Finally, we integrated the model into our live-streaming pipeline to automatically filter out unproductive queries in real-time.\n
Result:\n
The solution significantly improved the efficiency and quality of live-stream interactions. By reducing the number of irrelevant questions, we saved computational resources and allowed the digital human to focus on engaging meaningfully with users. This enhancement led to positive feedback from customers and a noticeable improvement in user satisfaction.""")

    with st.expander("What tools or systems did you use to ensure quality delivery in a complex project?"):
        st.write("""Situation:\n
In our digital human live-streaming project, we were developing a product that used large language models (LLMs) for generating live-stream scripts and supporting real-time audience interaction. The project was complex, involving multiple teams including machine learning engineers, infrastructure engineers, designers, product managers, and marketing teams. We needed to ensure high-quality delivery across all stages of development.\n
Task:\n
My task was to ensure that the product was delivered on time, met high-quality standards, and met the needs of both internal stakeholders and end-users, despite the complexity of integrating various technologies and working with cross-functional teams.\n
Action:\n
1. Agile Development: To manage the complexity and ensure consistent progress, we adopted Agile practices. We organized the project into sprints, with clear goals and deliverables for each phase. This allowed us to maintain focus, track progress, and quickly adapt to any changes or challenges that arose. We held regular sprint reviews and retrospectives to assess progress and identify areas for improvement.\n
2. Quality Assurance (QA) and Testing: We implemented a robust QA process to ensure the product's quality. This included automated testing for key components, such as the LLM fine-tuning and real-time audience interaction features. We also conducted manual testing for areas that required human judgment, such as user experience and script generation quality. We used tools like Jenkins for continuous integration and Selenium for automated UI testing, ensuring that new code didn’t introduce regressions.\n
3. Collaboration Tools: To facilitate smooth communication across teams, we used tools like Jira for task tracking, Confluence for documentation, and Slack for day-to-day communication. These tools allowed us to stay organized, track dependencies, and ensure that everyone had visibility into the project’s progress.\n
4. Code Reviews and Pair Programming: We emphasized the importance of code quality through regular code reviews. Engineers were encouraged to perform peer reviews to catch potential issues early and share best practices. Additionally, we adopted pair programming for critical parts of the project, particularly when integrating the LLM with the live-streaming infrastructure. This approach helped improve code quality and foster collaboration between team members.\n
5. Feedback Loops: We set up regular feedback loops with product managers, designers, and other stakeholders to ensure that the product aligned with user needs. This helped us identify potential issues early and make adjustments before they became larger problems. We also conducted user testing with a small group of end-users to gather insights on the product's performance and usability.\n
6. Monitoring and Performance Metrics: Once the product was deployed, we used monitoring tools like Prometheus and Grafana to track the performance of the live-streaming feature in real time. This allowed us to quickly identify and address any performance bottlenecks or issues that could affect the user experience.\n
Result:\n
By using these tools and systems, we were able to maintain a high standard of quality throughout the project. The product was delivered on time, met the functional requirements, and performed well in real-world use cases. The live-streaming feature became a key selling point for the product, and we received positive feedback from both internal stakeholders and customers. The success of this project also helped establish best practices for future projects and improved the overall development process within the team.""")

    with st.expander("How do you prioritize tasks and projects when your team is under tight deadlines?"):
        st.write("""When my team faces tight deadlines, I take a structured approach to prioritization: \n
1. Assess Tasks Based on Urgency and Impact:\n
  - I categorize tasks into four quadrants (urgent & high-impact, urgent & low-impact, non-urgent & high-impact, and non-urgent & low-impact). This helps identify critical tasks that need immediate attention while deferring less important ones.\n
  - I also consider dependencies, ensuring that blockers for downstream work are resolved first.\n
2. Align with Goals:\n
  - I cross-check tasks against the team’s quarterly OKRs and company priorities. If a task doesn’t contribute meaningfully to these goals, I deprioritize or postpone it.\n
3. Communicate Trade-offs:\n
  - Transparency is key. I involve stakeholders to discuss trade-offs, like reducing scope or extending timelines. For instance, during the digital human project, I had to delay secondary features to ensure the core product launched on time.\n
4. Empower the Team:\n
  - I encourage team members to raise concerns about workload or blockers. This ensures tasks are distributed evenly, reducing burnout while maximizing productivity.\n
5. Use Tools for Tracking:\n
  - Tools like JIRA or Asana help me visualize progress, reassign tasks dynamically, and avoid bottlenecks. Regular stand-ups and check-ins ensure alignment and progress tracking.\n
By following this method, I ensure the team delivers on deadlines without compromising quality or morale.""")

    with st.expander("Tell me about a time when you had to finish a task under a tight deadline."):
        st.write("""Sure! When we were working on the digital human live-streaming product, the company was getting ready to release our in-house large language model (LLM). We wanted to showcase our product as part of the launch, especially the real-time interaction feature, to show how the LLM could be used in action.\n
The deadline was tight, and we had a lot to figure out—making sure the real-time interaction was smooth, integrating the LLM, and preparing a demo that would impress both the company and potential customers.\n
To make it happen, we prioritized tasks carefully, focused only on what was absolutely necessary for the showcase, and worked closely as a team. For example, I made sure engineers, designers, and product managers were all aligned and constantly in sync. We even worked late a few nights to fix some tricky bugs.\n
In the end, we finished everything on time, and the demo went really well. The product’s real-time interaction feature was a big hit and showed off the LLM’s potential in a practical, exciting way. It was a great example of how we pulled together as a team under pressure and made something amazing happen.""")

    with st.expander("How do you make decisions when faced with incomplete or ambiguous information?"):
        st.write("""Decision-making in uncertain situations requires balancing speed and quality:\n
1. Gather Available Data:\n
  - I collect as much relevant data as possible within the given constraints. For example, during the early phases of developing the knowledge engine at CloudWalk, I relied on partial user feedback and historical project data to guide initial decisions.\n
2. Leverage Frameworks:\n
  - Decision Trees: I map out possible outcomes of each option, weighing their likelihood and impact.\n
  - Cost-Benefit Analysis: I compare the potential benefits of a decision against its risks and costs. For instance, when deciding whether to refactor the rendering engine for digital humans, this approach helped me justify the resource investment.\n
3. Consult Experts:\n
  - I leverage the expertise within my team or network. Collaborative brainstorming often surfaces perspectives I hadn’t considered, reducing ambiguity.\n
4. Emphasize Iteration:\n
  - I adopt an iterative approach, making incremental decisions where possible. By starting small, such as building a proof-of-concept, I gather insights that guide the next steps.\n
5. Document Assumptions:\n
  - I ensure all decisions are accompanied by documented assumptions. If outcomes don’t align with expectations, this helps in revisiting and refining the decision.\n
This approach enables me to act decisively, even in ambiguous situations, while minimizing the risk of failure.""")

    with st.expander("Tell me about a time you made decision with incomplete information."):
        st.write("""1. **Key summary:** \n
I made decisions by gathering as much relevant information as possible, analyzing risks and trade-offs, and using a phased approach to test and validate assumptions.\n  
2. **Details:**  \n
When we started developing the digital human live-streaming product, the concept of using large language models (LLMs) for live-stream script generation was new, and the market response was uncertain. We had limited data on how users would interact with the feature and whether it would truly solve their pain points.\n  
3. **Action taken:**  \n
- **Gathering information:** I conducted user interviews and market research to understand live-streaming pain points. Users consistently mentioned challenges in creating engaging and professional scripts, which gave us confidence in the core idea.\n  
- **Analyzing trade-offs:** Despite this input, there was still uncertainty about whether the auto-generated scripts would meet users' expectations. Instead of committing to a fully automated system immediately, we opted to combine automation with user input, turning the feature into a "co-pilot" where users could edit and enhance generated scripts.\n  
- **Phased rollout:** We developed an MVP with basic script generation and launched it to a small group of users to gather feedback. This allowed us to test our assumptions without investing too much time or resources upfront.  \n
4. **Results:**  \n
The phased approach helped us validate the feature while addressing ambiguity. User feedback showed that they valued the co-pilot feature because it saved time and offered creative suggestions while still allowing customization. This insight guided our development of more advanced features, like improving script personalization and fine-tuning the LLM for specific user needs.\n  
5. **Reflection:**  \n
This experience taught me the value of embracing uncertainty by making informed decisions and testing hypotheses early. Breaking complex challenges into smaller steps and validating them through real-world feedback reduces risks and allows for better outcomes.""")

    with st.expander("Tell me about a time you made decision with incomplete information. **Another example**"):
        st.write("""Situation:\n
When we were developing the real-time interaction feature for the digital human product, we faced a critical challenge due to the hallucination problem of large language models (LLMs). The LLM would sometimes generate inaccurate or irrelevant responses, which could harm the user experience and trust in the product. At the time, Retrieval-Augmented Generation (RAG) was emerging as a potential solution, but it was still relatively new, and there was uncertainty about how well it would perform in production or how the market would respond.\n
Task:\n
My goal was to ensure that the real-time interaction feature could provide accurate and reliable responses while mitigating the risk of LLM hallucinations. I needed to make a decision about whether to adopt the RAG approach despite the incomplete information and uncertainties surrounding its effectiveness and market acceptance.\n
Action:\n
I started by gathering information on the RAG approach, including reviewing existing research and talking to experts in the field to understand its potential benefits and limitations. After gathering this information, I carefully analyzed the trade-offs, considering the potential risks of adopting a new technology versus the opportunity to improve the product’s reliability. I decided to proceed with RAG, but I opted for a phased rollout. We began with a small-scale proof of concept, closely monitoring performance and user feedback. This allowed us to refine the system gradually, making adjustments based on real-world usage while minimizing the impact of potential issues.\n
Result:\n
The results were encouraging. RAG significantly reduced hallucinations, and user feedback was positive, highlighting the improved accuracy and reliability of the responses. Over time, we iteratively enhanced the knowledge base and fine-tuned the system, which led to a much better product experience. This decision not only addressed a critical technical challenge but also helped us differentiate our product in the market and gain user trust.""")

    with st.expander("What frameworks or principles guide your decision-making as a leader?"):
        st.write("""Several core principles guide my leadership decisions:\n
1. Data-Driven Approach:\n
  - Decisions should be backed by data whenever possible. For example, when deciding which features to prioritize for the digital human platform, I analyzed user behavior data and market research to ensure our efforts aligned with user needs and ROI.\n
2. Customer-Centric Focus:\n
  - I always consider the impact on end-users. If a decision improves user experience or solves a pain point, it takes precedence.\n
3. Iterative Improvement:\n
  - I believe in building incrementally and refining through feedback. For instance, during the live-streaming product development, we started with a simple MVP and enhanced it based on real-world usage data.\n
4. Sustainability and Scalability:\n
  - I balance short-term wins with long-term sustainability. Decisions must not only solve today’s problems but also remain adaptable for future growth. For example, when designing architecture for a high-throughput system, I plan for scalability, ensuring it can handle increased demand over time.\n
5. Team Collaboration and Ownership:\n
  - I involve the team in critical decisions to foster ownership and buy-in. A collaborative approach often results in better outcomes and higher morale.\n
6. Bias for Action:\n
  - While I value thorough analysis, I avoid decision paralysis. Taking timely, informed action is often better than waiting for perfect information.\n
7. Learning from Outcomes:\n
  - Post-decision reviews are integral. Whether a decision succeeds or fails, I analyze outcomes to improve future decision-making.\n
By adhering to these principles, I ensure my decisions are thoughtful, impactful, and aligned with both team and organizational goals.""")

    with st.expander("How to build creditability with teammates when you join a new team."):
        st.write("""When I join a new team, my first priority is to **listen and understand**. I take time to get to know the team dynamics, understand existing workflows, and learn from team members about their goals and challenges. This helps me build a foundation of trust, as people appreciate that I’m invested in understanding their processes and concerns before making any changes.\n
Next, I focus on **demonstrating my competence** *[ˈkɑːmpɪtəns]* by contributing meaningfully to projects and showing that I can add value. I avoid trying to impress or dominate discussions, but rather aim to offer solutions that are based on my knowledge and experience, while being open to feedback from others.\n
I also believe in building relationships with my teammates by showing genuine interest in their work and fostering a collaborative environment. By being approachable and engaging, I can earn their trust and create a strong team culture.\n
Being transparent and open is key in these early stages. I make sure that my goals and intentions are clear to the team and that I’m honest about what I can bring to the table. I also respect existing team processes and aim to work within them while identifying areas for improvement if needed.\n
Finally, I know that delivering results is one of the most important ways to build credibility. By consistently following through on commitments and delivering on my responsibilities, I earn the respect and trust of my teammates over time.""")

    with st.expander("Tell me about a time how did you work with people who might be technically excellent but hard to work with?"):
        st.write("""1. **Key summary:** \n
I improved collaboration by understanding the root cause of the challenge, fostering open communication, and aligning strengths with team goals.\n  
2. **Details:**  \n
When we started working on the digital human product, a backend engineer joined my team after a reorg. They were technically excellent, with a deep understanding of backend systems, but had a reputation for being difficult in team settings. Their strong opinions and focus on technical details sometimes made collaboration challenging.\n  
3. **Actions taken:**  \n
- **Understanding their perspective:** I scheduled one-on-one meetings to learn more about their concerns and motivations. I found that their behavior stemmed from a desire to ensure high technical standards and long-term maintainability of the system.\n  
- **Clear communication:** I acknowledged their expertise and emphasized that teamwork was essential to achieving the ambitious goals of our product. I also set clear expectations for collaboration and respectful communication with other team members.  \n
- **Inclusive environment:** During team discussions, I ensured they had the space to share their ideas while encouraging others to contribute as well. This balanced approach reduced friction and kept conversations productive.  \n
- **Constructive feedback:** I fostered an environment where feedback was encouraged. Regular check-ins allowed us to address any concerns early and ensure alignment with project objectives.  \n
4. **Results:**  \n
Over time, this approach helped improve the working relationship. The backend engineer’s contributions became a key asset to the team, and their insights significantly enhanced the scalability and reliability of the digital human product. We successfully launched on schedule, and the engineer became more integrated into the team dynamic.\n  
5. **Reflection:**  \n
This experience taught me the value of empathy, open communication, and focusing on shared goals. By taking the time to understand and address the concerns of a technically skilled but challenging team member, it’s possible to turn a difficult situation into a productive and successful collaboration.  """)

    with st.expander("Tell me about a time you solved a problem creatively."):
        st.write("""While working on the digital human product, we faced a challenge as users wanted to customize their own voices and avatars. Initially, with a small user base, the process was manual—users would send recordings via WeChat to our sales team, and our operations team would review the content to ensure quality. If the recordings didn’t meet the requirements, they had to be redone. Once approved, the recordings were passed to our machine learning engineers for custom model training. As the user base grew, this manual process became unscalable.\n
To address this, we developed a system that automated the entire process. Instead of relying on manual steps, we created a system where users could upload their audio and video recordings directly. The system provided step-by-step recording guides, and to make it engaging, we gamified the recording process—especially for audio, where there were more steps to follow. This made the experience less tedious for users.\n
On the backend, our operations team could review the uploaded content within the same system and provide feedback for improvements. Machine learning engineers were notified automatically when new training tasks were ready, and once the custom models were trained, they could be deployed with a single click. The system would then notify users that their personalized avatars were ready for use.\n
This automated solution not only scaled effectively with user growth but also enhanced the user experience and improved internal workflow efficiency.""")

    with st.expander("Tell me about a time how you encourage innovation while ensuring alignment with technical constraints."):
        st.write("""1. **Key summary:**\n
I encouraged my team to combine the digital human live-streaming platform with GenAI while respecting technical constraints, leading to impactful AIGC features.\n  
2. **Details:**  \n
While working on the digital human project, I encouraged the team to push the boundaries of innovation by integrating more GenAI capabilities. Beyond generating live-stream scripts, we explored features like live-stream background generation and video script creation using AIGC technologies. This not only enhanced the platform’s functionality but also helped us stand out in a competitive market.\n  
3. **Actions taken:**  \n
- **Promote exploration:** I allocated time for the team to experiment with new ideas. For instance, we prototyped different ways to generate live-stream backgrounds using diffusion models, which became a key feature.\n  
- **Set clear guardrails:** I defined constraints such as ensuring the platform worked on consumer-grade GPUs, which kept costs low. These constraints drove the team to optimize the rendering pipeline and improve system efficiency.\n  
- **Encourage knowledge sharing:** I fostered an open environment for sharing ideas through brainstorming sessions and tech talks. This collaboration often revealed innovative approaches while addressing potential challenges early.  \n
- **Celebrate wins and learn from failures:** When the first version of the background generator didn’t meet quality expectations, we analyzed the gaps, improved the training dataset, and refined the model. This iterative process made the final version a success.\n  
- **Iterative approach:** We built lightweight prototypes of each feature to test feasibility and gather feedback. This iterative strategy helped us focus on the most promising innovations while aligning with technical constraints.  \n
- **Cross-functional collaboration:** By involving product managers early, we ensured the new features met user needs and aligned with business priorities.  \n
4. **Results:**  \n
These AIGC features became a core part of our platform, significantly improving user satisfaction and positioning us ahead of competitors. The balance between encouraging creativity and respecting constraints enabled us to deliver innovative and practical solutions.\n  
5. **Reflection:**  \n
This experience demonstrated that fostering innovation within a structured framework allows the team to explore creative ideas while maintaining technical feasibility and alignment with organizational goals.""")

    with st.expander("Since you've managed sub teams, are you still technically hands on?"):
        st.write("""Yes, I consider myself still technically hands-on. During my time at Google as a Tech Lead Manager, it was a core part of the role to stay hands-on, and I brought that mindset to my role at CloudWalk. As my team grew from about 20 to over 30 members, I had more time to contribute technically when the team was smaller. For example, when we started the digital human project, I stepped in to design the initial architecture since we hadn't yet found the right architect.\n
Additionally, given how rapidly AI and large language models are evolving, I prioritize staying informed about the technical details, especially the boundaries and capabilities of these technologies. This allows me to guide the team effectively and ensure we’re making the right decisions as we push the limits of AI. \n
Although my day-to-day responsibilities involve more management, I make a conscious effort to stay technically involved, particularly in the early stages of projects and during key architectural decisions.  I try my best to join most design reviews, discuss technical details in meetings with engineers, lead group studies on new advancements in LLM, and always proactively experiment with new technologies. This approach ensures that I stay connected to the technical aspects while empowering my team with the latest knowledge and tools.""")

    with st.expander("How do you track and measure the success of your engineering team?"):
        st.write("""I use a combination of quantitative metrics and qualitative feedback to track and measure the success of my engineering team. Here’s how:  \n
1. **Delivery Metrics**: I measure the team’s ability to deliver on time and within scope. For example, during the development of the digital human product, we tracked sprint velocity, the number of features shipped, and the resolution of critical bugs to ensure we met project milestones.\n  
2. **Quality of Work**: Code quality and system reliability are key indicators. I track metrics such as test coverage, incident frequency, and user feedback. For instance, after optimizing the rendering resource scheduling pipeline, we saw a 5x improvement in efficiency, which validated the team’s technical success.\n  
3. **Team Productivity and Collaboration**: I assess productivity through task completion rates and cross-team collaboration effectiveness. Retrospective meetings help identify areas for improvement and foster continuous learning.\n  
4. **Impact on Business Goals**: I align the team’s performance with company or product outcomes. For example, the success of our digital human product—gaining over 10,000 paying users and generating millions in revenue—was a clear measure of the team’s impact.\n  
5. **Team Growth and Engagement**: I track individual development, promotions, and retention rates as indicators of a healthy team. I also gather feedback through one-on-ones to ensure team members feel supported and motivated.  \n
By combining these approaches, I ensure that my team is delivering value, growing professionally, and contributing to both short-term and long-term company goals.""")

    with st.expander("How do you ensure that your team is focusing on building scalable and sustainable solutions?"):
        st.write("""To ensure my team focuses on building scalable and sustainable solutions, I emphasize the following principles:  \n
1. **Start with Clear Requirements**: I ensure the team understands the long-term business needs and potential growth scenarios. For example, during the development of the digital human rendering platform, I emphasized scalability to support both small businesses and larger enterprises as the product gained traction.\n  
2. **Architect for Scalability Early**: I encourage designing systems with scalability in mind from the outset. For instance, we refactored our rendering engine system to handle real-time digital human rendering efficiently, optimizing the pipeline to accommodate more concurrent users without significant additional costs.\n  
3. **Leverage Best Practices**: I promote the use of proven frameworks, modular design, and cloud-native architectures to ensure systems are easy to extend and maintain. For example, in the RAG-based Q&A system, we used a microservices architecture to make individual components scalable independently.  \n
4. **Encourage Regular Refactoring**: I prioritize technical debt management by setting aside time for code reviews and refactoring. This ensures that short-term solutions don’t hinder long-term sustainability.  \n
5. **Monitor and Test Continuously**: I implement robust monitoring and load-testing practices to ensure systems perform well under expected and peak loads. For example, we stress-tested the digital human platform using simulated live-stream traffic to confirm it could handle spikes in demand.\n  
6. **Foster a Culture of Ownership**: I encourage the team to think beyond immediate goals, considering maintainability and scalability in every decision.  \n
These practices have consistently helped my teams deliver robust and future-proof solutions, balancing immediate deliverables with long-term sustainability.""")

    with st.expander("How do you ensure the solutions your team builds are extensible and maintainable?"):
        st.write("""Ensuring extensibility and maintainability requires a combination of technical practices, clear processes, and cultural reinforcement:\n
1. Design Principles and Architecture:\n
  - I promote modular, loosely coupled architectures. For example, in the digital human live-streaming platform, we built the script generation module as a standalone service with well-defined APIs, making it easy to upgrade or replace without affecting other components.\n
  - We follow best practices like domain-driven design and emphasize scalability early in the design phase.\n
2. Code Quality and Standards:\n
  - I enforce coding standards through linters, code reviews, and style guides.\n
  - Automated testing is mandatory for all components, including unit, integration, and regression tests, ensuring the system remains stable during changes.\n
3. Documentation and Knowledge Sharing:\n
  - Comprehensive documentation is non-negotiable. For example, when we refactored the rendering engine, detailed design docs ensured new team members could quickly onboard and contribute.\n
4. Regular Refactoring:\n
  - I schedule time for technical debt reduction and proactive refactoring. During the knowledge engine project, we allocated sprints to clean up legacy code, significantly improving maintainability.\n
5. Feedback Loops:\n
  - I conduct regular architecture reviews to evaluate if the system meets current and future needs. Cross-functional collaboration ensures solutions are practical and aligned with evolving requirements.\n
By embedding these practices, I ensure that solutions not only meet immediate needs but also remain adaptable as requirements evolve.""")

    with st.expander("Describe a time when you had to make a build-vs-buy decision for a key component in your system."):
        st.write("""During the development of the digital human live-streaming platform, we faced a critical decision about the speech synthesis module: should we build our own TTS (Text-to-Speech) engine or integrate an existing third-party solution?\n
1. Evaluate Requirements:\n
  - Our primary goals were high-quality voice output, real-time performance, and compatibility with our digital human system.\n
2. Assess Options:\n
  - Build: Building in-house would give us complete control and customization but required significant time and resources.\n
  - Buy: Third-party APIs like Google Cloud TTS or Azure TTS offered quick integration and good performance but at a recurring cost and limited customization.\n
3. Analysis:\n
  - I conducted a cost-benefit analysis, factoring in development time, licensing costs, and the expected lifespan of the feature.\n
  - A prototype integrating third-party TTS helped us evaluate latency and output quality.\n
4. Decision:\n
  - Initially, we chose to integrate a third-party solution to accelerate time-to-market. However, we began an in-house TTS development effort in parallel to address limitations (e.g., custom voice styles and languages).\n
5. Outcome:\n
  - The hybrid approach worked well: the third-party solution allowed us to launch quickly, and the custom engine replaced it later, reducing costs and increasing flexibility.\n
This experience highlighted the importance of balancing short-term needs with long-term goals.""")

    st.header("Managing team execution.")
    with st.expander("Tell me about a time how did you motivate your team to perform better?"):
        st.write("""To motivate my team to perform better, especially in a high-pressure environment like the digital human project where competition was tough, timelines were tight, and resources were limited, I employed several strategies:  \n
**1. Setting clear goals and priorities:** I ensured that everyone understood the project’s objectives and the critical milestones we needed to hit. For the digital human project, I emphasized the unique market opportunity we were tackling, which gave the team a sense of purpose and urgency. I also prioritized tasks effectively, so the team focused on high-impact work without feeling overwhelmed by the constraints.\n  
**2. Empowering ownership and autonomy:** I encouraged team members to take ownership of specific features or components of the product. For example, one engineer led the optimization of the rendering engine pipeline, which resulted in a huge efficiency improvement. This sense of ownership fostered pride in their contributions and kept motivation high, even during intense periods.  \n
**3. Recognizing achievements:** Despite the tight timeline, I made it a point to celebrate both small wins and major breakthroughs. For instance, when the scheduling center for real-time rendering was successfully implemented, I acknowledged the team’s hard work in meetings and highlighted their efforts to senior management, boosting morale and reinforcing the value of their work.  \n
**4. Supporting personal growth:** I took the time to understand each team member’s career aspirations. One junior engineer expressed interest in project management, so I assigned them tasks involving cross-team coordination, which aligned with their goals while benefiting the project. This alignment between personal growth and project needs kept the team motivated.  \n
**5. Leading by example:** I showed my commitment by stepping in to address gaps when resources were limited, such as designing the architecture for the project in its early stages. My hands-on involvement and willingness to tackle challenges alongside the team demonstrated my investment in our collective success, inspiring them to put in their best efforts.  \n
**6. Resolving obstacles:** I proactively worked to eliminate blockers. For instance, I negotiated additional GPU resources with senior management to address rendering bottlenecks, ensuring the team had the tools needed to deliver high-quality results on time.  \n
By combining these approaches, I created a supportive and purpose-driven environment where my team was motivated to overcome challenges and deliver an innovative, market-leading product.""")

    with st.expander("How do you manage multiple requests for your team, how do you deal with competing priorities?"):
        st.write("""Sure! At CloudWalk, I often had to manage multiple requests from different stakeholders while working on our digital human live-streaming product. One specific instance was when the product was in its early stages, and I was juggling requests from the product manager, marketing team, and engineering team, all with competing priorities.

Here’s how I handled it:

1. **Understand and Prioritize**: I started by gathering all the requests and breaking them down into specific tasks. For example, the product manager wanted a new feature to differentiate us in the market, the marketing team needed a demo for an upcoming event, and the engineering team needed time to address technical debt that was slowing development. I evaluated each request based on urgency, impact on the product, and alignment with our goals.

2. **Communicate Transparently**: I held a meeting with all stakeholders to share my understanding of their needs and explained the trade-offs. For example, I pointed out that if we focused on the marketing demo, the feature delivery might be delayed, but it could help attract early adopters. This open communication helped everyone understand the bigger picture.

3. **Create a Plan**: Based on the discussion, I developed a plan that balanced short-term and long-term goals. We decided to allocate time for the marketing demo first since it had a hard deadline, while simultaneously starting initial work on the new feature. For technical debt, I scheduled dedicated time in the following sprint to address it.

4. **Delegate and Monitor**: I delegated tasks based on team members’ strengths and ensured everyone was clear on their responsibilities. I also set up regular check-ins to track progress and quickly adjust if priorities shifted.

5. **Reflect and Learn**: After the marketing event, I reviewed the process with the team to see what worked and what could be improved for the next time. This helped us streamline how we managed competing requests going forward.

By staying organized, communicating clearly, and being flexible, I was able to meet the marketing deadline, make progress on the new feature, and address the technical debt in the next sprint. This experience taught me the importance of balancing immediate needs with long-term priorities and making sure everyone is aligned.""")

    with st.expander("Tell me about a time how did you setup projects for success?"):
        st.write("""Let me take the digital human project as an example, to set up it for success, I focused on three key areas: **defining success clearly**, **managing timelines effectively**, and **fostering strong communication and morale**.\n  
**1. Defining success clearly:**  \n
Before starting, I worked with all key stakeholders—engineers, product managers, and external teams—to ensure we had a shared understanding of what success looked like. For the digital human project, this meant creating a product that addressed customer pain points, hit tight deadlines, and aligned with our strategic goals. During this phase, I also identified dependencies, like the need for additional GPU resources, and planned to resolve these early to avoid delays.\n  
**2. Managing timelines effectively:**  \n
Given the intense competition and limited resources, I broke the project into clear, achievable milestones for each phase, such as script generation, rendering optimization, and QA. I worked closely with product and engineering teams to set realistic deadlines and assigned a senior engineer as the Directly Responsible Individual (DRI) for key technical tasks. Regular checkpoints allowed us to monitor progress, adjust plans when issues arose, and keep the team focused on delivering results step by step.\n  
**3. Fostering strong communication and morale:**  \n
I established regular standups to keep the team aligned and address any challenges early. For example, when there were disagreements about prioritizing 2D vs. 3D avatars, I facilitated discussions, gathered user feedback, and worked with management to resolve conflicts, keeping the team focused on shared goals. Celebrating small wins along the way, like successfully implementing real-time rendering, kept morale high and ensured everyone felt their contributions were valued.\n  
By combining clear goals, effective planning, and strong communication, we were able to navigate tight timelines and resource constraints, ultimately delivering a highly successful product.""")

    with st.expander("How do you balance feature development and technical debt?"):
        st.write("""Technical debt is a natural part of development, especially when moving fast, but it’s important to manage it before it becomes a bottleneck. I usually dedicate around 20% of our development time to addressing technical debt, focusing on issues that impact performance, scalability, and team productivity. I work closely with the team to identify key areas of friction, and whenever possible, we try to address technical debt during feature development to avoid taking separate time away. However, when the debt is too large or impactful, we plan dedicated sprints to tackle it.\n
For instance, during the development of our digital human platform, we initially reused an existing resource scheduling framework to generate digital human videos. While it allowed us to move quickly at first, it soon became clear that the framework was inefficient and prone to frequent errors, which slowed down the entire process. The team spent a significant amount of time troubleshooting, which took away from feature development. Recognizing the long-term cost, we made the decision to refactor the entire system and build a dedicated resource scheduling system specifically optimized for digital human rendering. This effort paid off — We significantly improved rendering efficiency, drastically reduced errors, and created more time for future feature development. It was a clear example of how investing time in addressing technical debt can unlock greater velocity and stability for the team.""")

    with st.expander("How do you explain tech debt to non technical team members?"):
        st.write("""When explaining tech debt to non-technical team members, I usually compare it to financial debt. Just like borrowing money can help you achieve something quickly but comes with the need to repay it with interest, tech debt arises when we prioritize speed over perfect code or optimal solutions. It helps us move fast in the short term, but over time, we accumulate “interest” in the form of maintenance issues, bugs, or slower development.\n
Addressing tech debt requires time and resources, just like repaying financial debt, but if we don’t tackle it, it can slow down future progress and make new feature development harder or riskier.""")

    with st.expander("How do you measure your impact as an engineering manager?"):
        st.write("""Measuring my impact as an engineering manager during the digital human project involved focusing on three main areas: **customer impact**, **organizational impact**, and **team impact**.\n  
**1. Customer Impact:**  \n
I assessed how our work directly benefited our customers by tracking metrics like user adoption, satisfaction, and engagement. For example, the digital human project’s script generation feature allowed users to create high-quality live-streaming content with minimal effort. I monitored user feedback and usage metrics to ensure the feature addressed real pain points. The fact that the product attracted over 10,000 paying users and generated significant revenue validated its impact on our customers.\n  
**2. Organizational Impact:**  \n
I evaluated how the project contributed to the company’s strategic goals. The digital human product was one of the few initiatives to reach the final stage of internal evaluation and became a major revenue driver, earning tens of millions annually. By delivering a solution that automated live-stream hosting, we not only opened up a new revenue stream but also strengthened the company’s position in the AI-driven digital content market.\n  
**3. Team Impact:**  \n
I measured how the project supported my team’s growth and productivity. For instance, I helped an engineer grow into a technical leadership role by letting them own the rendering engine optimization, resulting in a 5x improvement in efficiency. I also addressed technical debt early by redesigning our engine call framework, which reduced errors and improved team productivity. Regular one-on-ones ensured I stayed aligned with team members’ career goals and supported their development throughout the project.\n  
To track impact effectively, I used a mix of quantitative metrics (like revenue, adoption rates, and efficiency improvements) and qualitative feedback (such as team satisfaction and customer testimonials). By aligning project goals with customer needs, company strategy, and team growth, I ensured that my contributions had a meaningful and measurable impact.""")

    with st.expander("How do you approach balancing individual growth and team goals?"):
        st.write("""I believe that individual growth and team goals are not mutually exclusive but rather complementary. When team members grow, their contributions to the team naturally improve, which helps the team achieve its objectives.\n
To balance these priorities, I start by understanding each team member’s strengths, career aspirations, and development areas through one-on-ones and feedback sessions. I then align their growth with the team’s needs. For instance, if someone wants to improve their leadership skills, I might assign them as the lead for a critical project or a mentor for a junior team member. Similarly, if someone wants to deepen their technical expertise, I ensure they work on challenging technical problems that align with the team’s goals.\n
For example, during the development of the digital human product at CloudWalk, I noticed that one of my engineers was interested in transitioning to a more architectural role. I assigned them to lead the design of a new rendering pipeline, which was a key component of the project. This not only supported their growth but also significantly advanced the project by increasing the rendering efficiency.\n
By regularly checking in and adjusting responsibilities as needed, I ensure that individuals continue to grow while the team meets its objectives. This approach has helped me maintain a motivated team that consistently delivers results.""")

    with st.expander("How do you ensure your team is aligned with company or product goals?"):
        st.write("""To align my team with company or product goals, I focus on clear communication, connecting their work to the broader vision, and reinforcing alignment throughout the project lifecycle:\n  
1. **Translate High-Level Goals into Team Objectives**: I break down company or product goals into clear, actionable objectives for the team. For example, at CloudWalk, when the company shifted its focus to large model applications after ChatGPT’s release, I translated this strategic priority into a roadmap for our digital human live-streaming product. I ensured the team understood how this project fit into the company’s vision and growth strategy.\n  
2. **Communicate the “Why”**: I explain the purpose behind goals and how they align with market needs and company priorities. During our digital human project, I regularly reminded the team of the value we were delivering to users and how the product supported the company’s success.  \n
3. **Regular Review and Adjust**: I establish check-ins to review progress and ensure ongoing alignment. For example, in bi-weekly sprint reviews, I revisited goals, addressed roadblocks, and adjusted plans as necessary to stay on track. \n
4. **Empower Ownership**: I encourage team members to take ownership of their tasks, linking their responsibilities to company outcomes. This fosters a sense of purpose and accountability.  \n
5. **Celebrate Successes**: Highlighting how the team’s work contributes to achieving larger goals reinforces alignment and boosts motivation. For instance, when our digital human product achieved revenue milestones, I shared these wins with the team to emphasize their impact.\n  
This approach ensures my team stays focused, motivated, and aligned with overarching company or product goals.""")

    with st.expander("Creating Quarterly Team OKRs."):
        st.write("""When creating quarterly OKRs for my team, I start by reflecting on the purpose of OKRs and their role in aligning and motivating the team. Clear OKRs provide direction and a shared focus, which are crucial for driving team performance and achieving our objectives. Here’s how I approach the process:\n
1. Align with Company Goals: I begin by reviewing the company’s overarching goals and objectives. It’s important to understand these broader targets to ensure that our team’s OKRs are aligned with the company’s strategic direction. This involves engaging in discussions with leadership to grasp the high-level priorities and how they translate to our team’s focus.\n
2. Define Team-Specific Objectives: Based on the company goals, I then identify the specific objectives relevant to our team. I work closely with my team to pinpoint what we need to achieve in the upcoming quarter to support these broader goals. For instance, if the company is aiming to enhance user engagement, our team’s objectives might center around launching new features or improving user experience.\n
3. Set Measurable Key Results: With clear objectives in place, I collaborate with the team to establish key results that are measurable and attainable. I ensure these key results are specific, quantifiable, and challenging yet realistic. For example, if our objective is to increase feature adoption, key results might include metrics such as user growth percentages, engagement rates, or feature usage statistics.\n
4. Foster Team Involvement and Ownership: I involve the team in the OKR-setting process to foster a sense of ownership and commitment. We brainstorm milestones and targets together, ensuring everyone understands and agrees on the path forward. To enhance accountability, I assign Directly Responsible Individuals (DRIs) for each key result, while emphasizing that the overall success is a collective responsibility.\n
5. Communicate and Commit: Once the OKRs are defined, I make sure they are clearly communicated to the entire team and to management. This includes outlining how these OKRs align with our team’s contribution to the company’s goals and ensuring that everyone is on the same page. Regular check-ins and updates are scheduled to track progress and adjust as needed.\n
6. Monitor and Review: Throughout the quarter, I track progress against our OKRs, using both quantitative metrics and qualitative feedback. This ongoing review helps identify any challenges early and allows us to pivot or adjust our strategies as necessary. At the end of the quarter, I conduct a thorough review to assess achievements and areas for improvement, which informs the next cycle of OKRs.\n
By following this approach, I ensure that our quarterly OKRs are not only aligned with company goals but also meaningful and motivating for the team, driving both individual and collective success.""")

    with st.expander("How do you set goals for your team?"):
        st.write("""I take a structured approach to ensure alignment with organizational objectives and address the team’s needs and capabilities.\n
**Gather Inputs**: I start by aligning with senior leadership to understand company goals, gather feedback from internal customers through surveys, and collect insights from my team on technical challenges and opportunities.\n
**Plan and Prioritize**: Using this data, I create and prioritize a list of goals based on impact and feasibility, considering KPIs like scalability, security, and balancing innovation with tech debt.\n
**Define and Communicate Goals**: I set clear, actionable goals, often using OKRs or roadmaps, and include stretch goals to motivate the team with ambitious targets.\n
**Execution and Review**: I ensure capacity planning aligns with goals and monitor progress through regular check-ins. If issues arise, we conduct blameless retrospectives to learn and improve.\n
**Motivation and Support**: I maintain transparent communication about goal prioritization and align tasks with team members' interests and career growth opportunities, framing even challenging tasks as learning experiences.\n
This approach ensures well-rounded, achievable goals that drive both team and personal development.""")

    st.header("Hiring and building team")
    with st.expander("How do you identify and hire top talent for your team?"):
        st.write("""I start by clearly defining the role and identifying both technical and soft skills critical for success. In the U.S., I rely heavily on platforms like LinkedIn, Indeed to source candidates, whereas in China, I use platforms like Boss Zhipin and Linpin to access local talent pools. I also encourage referrals and participate in industry events to broaden the talent pipeline. \n
At Google, the hiring process was highly structured, with standardized interview questions, rigorous rubrics, and a strong emphasis on leveraging the team-matching process to ensure a good fit for both the candidate and the team. At CloudWalk, while the hiring process was more flexible, I implemented structured interviews to reduce bias and ensure consistency. \n
I focus on assessing problem-solving skills, collaboration, and alignment with team values through behavioral and technical interviews. For senior roles, I place additional emphasis on leadership potential and strategic thinking.""")

    with st.expander("Can you describe a time when you had to hire for a role that required skills you were not familiar with?"):
        st.write("""When I needed to hire a UI designer for the digital human product, I wasn’t deeply familiar with the field. \n
To bridge the gap, I consulted with our product manager and external design consultants to understand the key skills and portfolio characteristics that would indicate a strong candidate. I also invited experienced designers from other teams to join the interview panel, ensuring we could thoroughly evaluate technical skills such as visual design, user experience principles, and prototyping. \n
Additionally, I educated myself by studying successful UI designs in similar products and familiarizing myself with common design tools like Figma and Adobe XD. This collaborative and well-researched approach helped us hire a designer who not only had strong technical skills but also a creative vision that aligned well with our product goals.""")

    with st.expander("Tell me about a time when you had to make a difficult hiring decision."):
        st.write("""When I needed to hire an architect for our digital human product, I faced a difficult decision between two strong candidates. \n
One had a longer tenure and slightly stronger technical expertise but lacked soft skills, while the other demonstrated strong leadership potential and communication skills but was slightly less technically experienced. \n
After careful consideration and discussions with my team, I chose the latter candidate because the role required not only technical expertise but also collaboration with cross-functional teams and the ability to guide others.\n 
I supported their technical growth through mentorship and additional resources, and they quickly ramped up, eventually becoming a key contributor and an influential leader in the project.""")

    with st.expander("Can you describe a time when you had to make a tough decision between hiring externally or promoting internal talent?"):
        st.write("""At CloudWalk, when building the team for our digital human product, I faced a tough decision between promoting an internal product manager or hiring externally. The internal candidates were experienced and familiar with the company’s processes, but their expertise was in B2B products. The digital human product, however, was consumer-facing and required a deep understanding of user engagement and the live-streaming e-commerce market, which was a completely different skill set.\n  
After careful consideration, I decided to hire externally to bring in a product manager with strong consumer-facing experience. This external hire had a proven track record of building successful consumer products and a deep understanding of user behavior, which were critical for the success of this project.  \n
To ensure alignment with internal processes, I facilitated their onboarding by pairing them with internal team members for knowledge sharing and provided context about the company’s strategic goals. This decision proved effective as their expertise helped us craft a user-centric product that gained over 10,000 paying users and generated significant revenue.""")

    with st.expander("What attributes do you look for in senior engineer candidates?"):
        st.write("""When evaluating senior engineer candidates, I look for a combination of technical expertise, problem-solving ability, collaboration skills, and leadership potential. Specifically:\n
**Technical Depth and Breadth**:\n
A senior engineer should have strong technical skills in their domain, along with a broad understanding of adjacent areas. For example, in our digital human project, a senior machine learning engineer not only needed expertise in NLP and LLMs but also an understanding of how their work integrates with backend systems and rendering pipelines.\n
**Problem-Solving and Ownership**:\n
I value engineers who can independently tackle complex problems, propose innovative solutions, and take ownership of their work. They should be proactive in identifying potential issues and driving solutions without needing constant direction.\n
**Collaboration and Communication**:\n
Strong communication skills are critical. Senior engineers often work cross-functionally with product managers, designers, and other teams. They should be able to explain technical concepts to non-technical stakeholders and mentor junior engineers effectively. For example, I’ve seen successful senior engineers facilitate discussions that bridge gaps between engineering and product teams.\n
**Leadership and Mentorship**:\n
A great senior engineer doesn’t just focus on their own work but also uplifts the team. I look for candidates who can mentor junior engineers, contribute to team culture, and lead by example. Leadership doesn’t always mean managing people—it’s about influencing others and driving positive outcomes.\n
**Adaptability and Growth Mindset**:\n
Technology evolves quickly, so I value candidates who are curious, eager to learn, and open to feedback. For instance, in our projects involving large language models, the technology changed rapidly, and adaptability was key to staying ahead.\n
In interviews, I assess these attributes through technical problem-solving tasks, behavioral questions, and discussions about their past experiences. I also pay attention to how they approach challenges and interact during collaborative exercises.""")

    with st.expander("How do you balance hiring externally versus promoting or developing internal talent?"):
        st.write("""I believe in promoting internal talent whenever possible because it boosts morale, retains institutional knowledge, and shows team members that their growth is valued. I regularly assess team members' readiness for new challenges and provide growth opportunities through stretch assignments and mentorship. \n
However, hiring externally has the benefit of bringing fresh perspectives and new expertise, which can be particularly valuable in addressing skill gaps or driving innovation. If there is a rapid growth in the team’s scope or responsibilities, I also prioritize external hires to quickly scale the team and ensure we can meet the demands of the expanded scope.""")

    with st.expander("How do you assess soft skills during the interview process?"):
        st.write("""I design behavioral interview questions to evaluate communication, collaboration, and problem-solving skills. For example, I ask candidates to describe a time they handled a conflict in a team or how they influenced others without direct authority. These questions help uncover how candidates navigate interpersonal challenges, build consensus, and approach difficult situations.\n
To ensure a well-rounded assessment, I involve multiple interviewers, each focusing on specific aspects of soft skills such as teamwork, adaptability, and empathy. This collaborative approach provides diverse perspectives and helps minimize individual biases, leading to a more accurate evaluation of the candidate’s interpersonal abilities.\n
Additionally, I pay close attention to how candidates communicate during technical problem-solving exercises. The way they explain their thought process, seek clarification, and respond to feedback serves as an implicit assessment of their soft skills. For instance, a candidate who actively engages in a discussion, incorporates suggestions, and remains composed under pressure demonstrates strong communication and collaboration abilities.\n
By combining structured behavioral questions, a multi-interviewer approach, and observation during technical exercises, I ensure a comprehensive evaluation of a candidate’s soft skills, identifying individuals who can contribute effectively to both the team and the organization.""")

    with st.expander("Have you ever had a bad hire, and how did you address the situation?"):
        st.write("""When I started at CloudWalk, I hired an engineer who seemed like a great fit on paper. They were super strong technically and had all the right skills. But once they joined, it became clear that working with others wasn’t their strong suit. They often had disagreements with teammates, dismissing their ideas and causing friction, which started to affect the overall team dynamic.\n
I didn’t want to ignore the problem, so I had a direct conversation with them. I gave specific examples of where things went wrong and explained how their behavior was impacting the team. I also offered suggestions on how to improve, like being more open to others’ ideas and focusing on better communication. We set clear goals and checked in regularly to see how things were going.\n
Unfortunately, even with all the feedback and support, nothing really changed. It got to a point where it was affecting everyone else, so I worked with HR to transition them out of the role. It wasn’t an easy decision, but it was the right one for the team.\n
Looking back, it was a big learning moment for me. I realized it’s not just about hiring people with the right technical skills—it’s just as important to find people who can work well with others. After that, I updated our hiring process to include more behavioral questions and made sure multiple interviewers were involved to get a better read on soft skills and cultural fit. It’s made a huge difference since then.""")

    with st.expander("What is your strategy for onboarding new hires effectively?"):
        st.write("""I start by creating a tailored onboarding plan that includes clear goals for the first 30, 60, and 90 days. I assign a mentor or buddy to help the new hire acclimate to the team and ensure they have access to necessary resources. I also schedule regular check-ins to provide feedback, answer questions, and address challenges. This approach helps new hires feel supported and productive quickly.\n
When I first joined Google, I started a 'Noogler' documentation to document my learning journey and onboarding experience. This document became a valuable resource for every new hire after me and was continuously enhanced by each new Noogler. At CloudWalk, I introduced the same practice, asking new hires to document their onboarding experience and update the guide to ensure it stays relevant and useful. This not only helps new hires feel supported and productive quickly, but also creates a culture of continuous improvement and shared knowledge.""")

    with st.expander("How do you handle high-volume hiring while maintaining quality?"):
        st.write("""As an engineer, my experience taught me only distributed systems can handle high-volume problems. I prioritize scalability by implementing a distributed and streaming approach to handle high-volume hiring effectively. \n
For example, I standardize interview questions and rubrics to ensure consistency, use automation tools to filter resumes, and integrate online assessment tools for an initial evaluation of candidates' technical and problem-solving skills.\n 
I also set up an interviewer pool by training a group of team members to conduct interviews, enabling us to scale the process while maintaining quality. \n
Additionally, I work closely with recruiters to align on the most critical skills and competencies, ensuring that every stage of the process remains focused and efficient.""")

    with st.expander("How do you ensure diversity and inclusion in your hiring process?"):
        st.write("""Ensuring diversity and inclusion in hiring is a priority for me because it leads to stronger teams and better outcomes. Here’s how I approach it:  \n
1. **Crafting Inclusive Job Descriptions**: I work with HR to ensure job postings are clear, free from biased language, and accessible to a broad range of candidates. This includes focusing on skills and potential rather than overly specific qualifications that might exclude capable individuals.\n  
2. **Expanding Candidate Pools**: I make an effort to reach diverse talent pools by partnering with organizations, attending events, and leveraging platforms that focus on underrepresented groups in tech.  \n
3. **Structured and Fair Interview Process**: I use structured interviews with standardized questions and evaluation criteria to minimize unconscious bias. I also ensure interview panels are diverse to provide different perspectives and create a welcoming environment for candidates.\n  
4. **Training and Awareness**: I advocate for interviewer training on unconscious bias and inclusive practices, helping the team understand how to assess candidates fairly and equitably.  \n
5. **Focus on Growth Potential**: I prioritize hiring for potential, not just current skills, which opens opportunities for candidates from non-traditional backgrounds who bring fresh perspectives and adaptability.\n  
6. **Post-Hire Support**: Diversity doesn’t stop at hiring. I ensure new hires are supported with onboarding programs and inclusive team dynamics, fostering a sense of belonging from day one.  \n
By embedding these practices, I aim to build a team that not only reflects diverse backgrounds and perspectives but also thrives through collaboration and innovation.""")

    with st.expander("How do you manage expectations between recruiters and hiring managers?"):
        st.write("""Managing expectations between recruiters and hiring managers is critical to ensuring a smooth and effective hiring process. Here’s how I approach it:  \n
1. **Clear Alignment on Goals**: At the start of the hiring process, I meet with the recruiter to align on the role’s requirements, priorities, and timelines. This includes discussing the ideal candidate profile, must-have versus nice-to-have skills, and any specific challenges we might face in the search.\n  
2. **Transparent Communication**: I maintain open and regular communication with recruiters, providing timely feedback on candidates and discussing any changes to the role or priorities. This ensures we stay on the same page throughout the process.  \n
3. **Realistic Timelines and Metrics**: I set realistic expectations about the hiring timeline and emphasize quality over quantity. For example, I’d rather wait a little longer for the right candidate than rush to fill the position.  \n
4. **Educating on Market Realities**: I rely on recruiters to provide insights about the talent market, such as availability of skills, compensation benchmarks, and competitive factors. This helps hiring managers adjust expectations when needed.\n  
5. **Collaborative Problem-Solving**: If challenges arise, such as a limited candidate pool or high decline rates, I work with recruiters to adjust strategies. This might include revisiting the job description, expanding the search criteria, or exploring new sourcing channels.\n  
6. **Respect for Expertise**: I respect the recruiter’s expertise in sourcing and candidate engagement while ensuring they understand the team’s technical and cultural needs. This mutual respect fosters a productive partnership.  \n
By fostering open communication, collaboration, and mutual understanding, I ensure recruiters and hiring managers work effectively together to achieve our shared goal: hiring the best talent for the team.""")

with tab3:
    with st.expander("Tell me about a project you are proud of."):
        st.write("""I’m particularly proud of a project I led at CloudWalk, where we developed a digital human live-streaming product. CloudWalk is an AI company that traditionally focused on B2B and government clients, but we saw an opportunity to leverage the growing interest in large language models, especially after the rise of ChatGPT, to explore consumer-facing applications.\n
The idea came about while we were working on a knowledge engine product for enterprise clients. We had a few e-commerce clients in the live-streaming industry who needed intelligent customer service solutions. This sparked an idea: in China, live-streaming e-commerce is huge, but it's also very expensive to hire human hosts, and the barriers to entry are high. We thought, why not build a solution where digital humans could assist or even partially replace live hosts?\n
We created a product that allows users to select a virtual host’s appearance and voice, generate product scripts automatically, and even set up interactive features to engage with viewers. This product became incredibly successful and was adopted as a core strategic application within the company, generating millions of RMB in revenue. It’s one of the projects I’m most proud of because it not only solved a real problem in the market but also demonstrated the power of AI-driven innovation.""")

    with st.expander("What's the feature of this product?"):
        st.write("""The digital human live-streaming product has the following key features:  \n
1. **Customizable Virtual Hosts**:  \n
   Users can select and customize virtual hosts’ appearances and voices, tailoring them to match their brand and audience preferences.\n  
2. **Automated Script Generation**:  \n
   The platform uses LLMs to generate engaging product scripts from simple inputs, which users can edit to ensure alignment with their needs.\n  
3. **Interactive Viewer Features**:  \n
   To foster real-time interaction, the product includes features like automated Q&A. Viewers can ask questions during the live stream, and the system, powered by Retrieval-Augmented Generation (RAG), extracts relevant answers from pre-uploaded product documents or FAQs.\n  
4. **Seamless Integration**:  \n
   The product integrates with major live-streaming platforms and supports easy setup for businesses of all sizes.\n  
5. **Cost-Effective Scalability**:  \n
   Optimized rendering pipelines enable use on consumer-grade GPUs, lowering costs and making the technology accessible to small businesses.  """)

    with st.expander("Why did you decide to initiate the project?"):
        st.write("""I decided to initiate the digital human product because I saw a clear opportunity in the live-streaming e-commerce space. Through my research, I noticed several pain points in the industry, especially in China—live hosts are expensive, and it’s tough for smaller businesses to break in. With the rise of large language models (LLMs) and advancements in AI, it became clear that we could automate much of the live-streaming process, from creating personalized virtual hosts to generating scripts and interactive features.\n
I also saw that this digital human product fit perfectly with the growing demand for scalable, AI-powered solutions. By combining the intelligence of large language models with digital humans—where AI acts as the "brain" and the humans as the "body"—we could reduce costs while engaging audiences in ways traditional methods just can't match. This approach allows businesses to connect with their customers in a more dynamic and cost-effective way, while solving real-world challenges.\n
In the end, the decision came down to the potential for a big market impact. It not only helps reduce the overhead of live-streaming but also positions the company as a leader in AI innovation within the entertainment and e-commerce sectors.""")

    with st.expander("What made the project technically interesting or complex."):
        st.write("""What made the project technically interesting and complex was the combination of optimizing cost, technology, and achieving product-market fit. One of the key challenges was ensuring the digital human could be rendered in real-time with affordable hardware. We optimized the rendering engine pipeline and built a specialized resource scheduling system to maximize machine utilization, which allowed us to use consumer-grade GPUs like the 3080 Ti for real-time rendering. This drastically reduced costs while maintaining high-quality output.\n
Another complex aspect was using large language models to generate live-stream scripts. When we started the digital human project, GPT-4 hadn't been released yet, and we tested all available models at the time, including API calls to closed-source models and open-source options. However, none of them produced satisfactory results, as live-streaming scripts require a unique, passionate tone that engages viewers and drives purchase intent. To address this challenge, we decided to continue training our company's in-house large language model, tailoring it specifically for live-stream scenarios. We crawled a vast amount of live-stream videos to train a base model and then fine-tuned it with high-quality, manually annotated data. The model's ability to generate scripts improved continuously through an integrated user feedback mechanism. We designed the product to allow users to input a few key points or keywords, based on which the model would automatically generate a script. Users could then modify the generated script to fit their preferences. These user-modified scripts were collected as feedback and fed back into the training data, enabling continuous improvement of the model. \n
Lastly, we implemented real-time audience interaction using a Retrieval Augmented Generation (RAG) approach. Unlike competing products that rely on pre-set Q&A templates, which are often limited in scope and lead to poor live-streaming experiences, we aimed to fully leverage the power of large language models. However, directly allowing the LLM to interact with the audience posed risks of hallucination, which could result in serious errors during live interactions. To address this, we built an automated system that allowed users to upload product-related documents, which were indexed in our system. During the live stream, the system would retrieve and rank relevant content in real-time, ensuring that responses were accurate and contextually appropriate. To continuously improve the product's interactivity, after each live stream, we generated a detailed report analyzing the interactions and audience engagement. This report allowed users to assess the effectiveness of the Q&A system and provide feedback. We used this feedback to enhance both the retrieval process and the model’s response generation, ensuring that the system became more accurate and interactive over time.""")

    with st.expander("How did you set up your team for success with this project."):
        st.write("""Before assembling the team, I first presented the project vision to the entire group. I gathered feedback and took into account each team member's preferences and strengths. This allowed me to organize the team in a way that aligned with their skills and interests. I also made sure that handovers were carefully managed so that our existing projects wouldn't be disrupted.\n
Once the team was in place, I brought in a mix of product managers, front-end and back-end engineers, and machine learning engineers to focus on the digital human live-streaming product. I helped key members, including an architect and several engineers, grow through the project, leading to their well-deserved promotions. Additionally, we collaborated with external teams—such as the speech, digital human rendering, and foundational large language model teams—to bring in specialized expertise, which was crucial for the project's success.\n
Similarly, before we began working with external teams, I clearly communicated our project plan and timeline. We secured the necessary resources from teams specializing in speech, digital human rendering, and foundational large language models. Throughout the project, I maintained open lines of communication with these teams, allowing us to make adjustments whenever needed to stay aligned and ensure smooth collaboration.""")

    with st.expander("Were there any conflicts during the project? How did you resolve them?"):
        st.write("""Yes, we faced both internal and external conflicts during the project. Internally, there was a disagreement between the product manager and the engineers. The product manager wanted to prioritize the integration of a large language model as a unique market differentiator, but the engineers felt this was too difficult to achieve in the short term. To resolve this, I proposed splitting the project into phases, allowing us to deliver an initial version while continuing to work toward the more complex features in later phases. This kept both sides satisfied and aligned.\n
Externally, there was a debate over whether we should focus on 2D or 3D digital humans. After analyzing user needs and market feedback, it became clear that 2D digital humans would better suit our immediate goals. I communicated this with senior management and external teams, ultimately convincing them to allocate more resources to support 2D digital humans. This helped us stay focused and ensured the product’s success.""")

    with st.expander("What was the outcome of the project?"):
        st.write("""The project was very successful. Internally, out of around ten projects that were initiated, it was one of only two that made it through to the final stage. Externally, it has attracted over 10,000 paying users and currently generates tens of millions of RMB annual revenue for the company. This success solidified the product's strategic importance and demonstrated its significant impact on both the company and the market.""")

    with st.expander("What's the work style difference knowledge engine project and digital human project?"):
        st.write("""The biggest difference between the two projects is the type of customers they serve. The knowledge engine is an infrastructure platform project, supporting other internal teams to deliver solutions to B2B clients or government clients. This means we're often in the background, helping various teams meet their specific project requirements. On the other hand, the digital human product is consumer-facing, directly targeting end-users or small businesses, so our focus shifts to understanding and catering to the needs of individual consumers.\n
In terms of work style, the knowledge engine requires close collaboration with different internal teams to deliver multiple projects at once. Since we're not the ones directly facing the customers, our challenge is managing the priorities and deadlines of multiple projects simultaneously. It's a lot of cross-team coordination and balancing resources to ensure smooth delivery. For the digital human product, however, we own the entire product end-to-end. This requires us to secure resources internally, iterate quickly, and work closely with marketing and sales to get the product out to the market. The focus is more on speed and ensuring the product evolves with consumer needs.\n
Finally, the product expectations are different. For the knowledge engine, our main priority is delivering on promised functionality to support B2B or government requirements, where reliability and fulfilling commitments are key. But with the digital human product, the bar is even higher. To succeed in the consumer space, the product needs a clear value proposition and unique selling points that make it stand out, giving users a compelling reason to choose it.""")

    with st.expander("What could you do better if you could do it again?"):
        st.write("""If I had the opportunity to do the project again, one improvement would be in the initial resource planning. For example, at the start, we were missing some key roles like a UI designer. Later, once we hired a professional UI designer, we had to spend significant time redesigning elements that could have been set up correctly from the beginning. Ensuring we had the right team in place from the start would have made the process more efficient.\n
Additionally, in terms of integrating the large language model (LLM), we initially fine-tuned an open-source model like LLaMA, but the results weren't ideal. Eventually, we decided to incorporate more live-streaming data directly during the training phase of our foundational LLM. This significantly improved the model's ability to generate live-streaming scripts, which could have been addressed earlier to enhance quality from the start.""")

    with st.expander("What do you want to do to enhance the product if you continue to work on it?"):
        st.write("""There are four key areas I’d like to focus on for enhancing the digital human product:  \n
### 1. **Improving Visual Quality**  \n
Currently, our solution based on Wav2Lip is approaching its limits. While it works well for simple lip-syncing, it doesn’t capture more complex expressions or gestures. Diffusion-based methods, which are emerging in research, offer a way to generate not only matching lip movements but also facial expressions and even body movements, taking the realism to a whole new level. Although these methods aren't yet widely adopted in industry due to cost and rendering speed, I believe continuing to explore and optimize them will lead to a major leap in quality.\n  
### 2. **Enhancing Script Generation**  \n
While the current scripts generated by our language model are functional, they often lack the nuance of human creativity and personality. I would refine the model to produce more personalized and stylized scripts that align with the specific brand or persona of the digital human. Incorporating user-defined stylistic parameters and expanding the fine-tuning dataset with branded content would allow the scripts to feel more aligned with user goals and improve their engagement value.\n  
### 3. **Improving Automatic Response Generation**  \n
The automatic responses generated during live interactions can sometimes feel mechanical or off-target. To address this, I would focus on significantly enhancing query understanding, retrieval, and reranking. This involves improving our fine-tuned models for intent classification and query rewriting to ensure the system fully grasps user input, even when queries are vague or ambiguous. On the retrieval side, I aim to refine our multi-channel retrieval framework by further optimizing the embedding model and incorporating domain-specific adaptations. For reranking, I would fine-tune our BGE-reranker using human-labeled data, ensuring the most contextually relevant results are prioritized. \n  
### 4. **Building a User Community Platform**  \n
As more users adopt the digital human product, I’d like to create a platform where they can share their creations, such as videos or live streams. This would allow users to see each other’s work, foster creativity, and increase engagement. A community-driven platform could also serve as a way for users to learn from each other and grow their capabilities, leading to a more active and loyal user base.\n  
These improvements would collectively make the product more engaging, versatile, and valuable to its users.""")

    with st.expander("How does wav2lip work."):
        st.write("""Wav2Lip is a deep learning model designed to generate realistic lip-sync for a given video based on audio input. Here’s an explanation of its working principle:\n
Wav2Lip works by taking two main inputs: a video of a person and an audio clip, which can be speech or any form of vocal sound. Its goal is to modify the mouth movements in the video so that they perfectly match the given audio.\n
The key technical aspects of Wav2Lip are:\n
1. Encoder-Decoder Architecture: It uses an encoder-decoder architecture where the audio and video are processed separately at first. The audio input is encoded into a feature representation that captures the phonetic content (the sounds that make up speech), while the video is processed to extract keyframes and focus on the facial regions, especially the mouth.\n
2. Lip-Sync Discriminator: The model includes a lip-sync discriminator, which is a type of neural network trained to judge whether the lip movements in the video are in sync with the audio. This discriminator plays a critical role by giving feedback to the generator, ensuring that the model produces lip movements that match the spoken words accurately.\n
3. GAN-based Training: Wav2Lip leverages Generative Adversarial Networks (GANs), where the generator creates lip-synced frames, and the discriminator evaluates how real or fake the sync appears. The competition between these networks helps improve the model's ability to generate highly realistic, lip-synced videos.\n
4. Frame-by-Frame Prediction: For each frame in the video, Wav2Lip generates new lip movements that match the audio, creating a seamless result that looks like the person in the video is speaking the given audio. The model can do this frame-by-frame without requiring any manual intervention.\n
By combining these techniques, Wav2Lip achieves impressive results in creating realistic lip-syncing for a variety of speakers and languages.""")

    with st.expander("How to evaluate wav2lip model?"):
        st.write("""Evaluating the Wav2Lip model, or any lip-sync model, involves both subjective and objective metrics to ensure it produces realistic and accurate lip movements in sync with audio. Here’s how you can approach evaluating Wav2Lip:\n
1. Lip-Sync Quality\n
- Lip-Sync Error (LSE): This is a common metric for evaluating lip-sync models. It calculates the difference between the actual lip movements and the predicted ones. The lower the LSE, the better the model's ability to sync lips with speech.\n
- Lip-Sync Confidence Score: Wav2Lip's own discriminator model can generate a confidence score that indicates how well the lip movements match the given audio. A higher score suggests a more accurate sync.\n
- Visual Inspection: Manual review of the lip-sync quality by watching the video to see how natural the synchronization feels.\n
2. Visual Realism\n
- Frame Perceptual Quality: Assessing the realism of the generated video frames. Even though Wav2Lip is focused on lip-sync, the overall video quality (e.g., facial expressions, smoothness of transitions) should be high.\n
- PSNR/SSIM (Peak Signal-to-Noise Ratio/Structural Similarity Index): These metrics can be used to compare the visual quality of the generated video with the original video. PSNR measures the difference in pixel values, while SSIM assesses the structural similarity between two images.\n
3. Speech Consistency\n
- Phoneme-to-Viseme Mapping Accuracy: Evaluate how accurately the model matches phonemes (units of sound) with visemes (lip shapes). A misalignment between the two will result in unnatural lip movements, so it’s important that they match closely.\n
- Word Error Rate (WER) for Speech Recognition: By running automatic speech recognition (ASR) on the audio-visual output, you can check whether the lip movements match the spoken words accurately. A lower WER indicates better consistency.\n
4. Naturalness and User Satisfaction\n
- User Study (MOS – Mean Opinion Score): Conducting human evaluations, where participants rate the naturalness and lip-sync quality of the videos on a scale (e.g., 1 to 5). This provides a subjective measure of how real and smooth the output looks to the average viewer.\n
- A/B Testing with Other Models: Comparing the Wav2Lip output against other lip-sync models to see how well it performs in terms of visual realism and lip-sync quality.\n
5. Generalization Across Domains\n
- Robustness Testing Across Different Speakers, Languages, and Noisy Audio: Since Wav2Lip should work across a variety of domains (different speakers, languages, and audio conditions), you can evaluate how well the model generalizes to new inputs. Testing it on different datasets helps ensure robustness.\n
- Cross-Domain Adaptability: Check how well Wav2Lip adapts to different lighting conditions, facial orientations, and camera angles. The model should ideally produce good results in a variety of visual settings.\n
6. Inference Speed and Resource Efficiency\n
- Latency/Inference Time: Measure how fast the model can generate lip-synced frames for a given audio input. This is especially important for real-time applications.\n
- Computational Efficiency: Evaluate the model’s computational requirements in terms of memory and processing power to ensure it can run on target hardware (e.g., edge devices or consumer-grade hardware).\n
By combining these quantitative and qualitative evaluations, you can get a comprehensive picture of how well Wav2Lip is performing and where improvements might be needed.""")

    with st.expander("Compare GAN-based models like Wav2Lip, Diffusion models, and Transformers."):
        st.write("""Here’s a comparison of **GAN-based models like Wav2Lip**, **Diffusion models**, and Transformers for lip-sync tasks, focusing on their distinct approaches and trade-offs:\n
1. GAN-based Models (e.g., Wav2Lip)\n
- Approach: Wav2Lip uses a Generative Adversarial Network (GAN) to generate realistic lip-syncing by mapping the audio to corresponding mouth movements. GANs consist of two networks: a generator that creates lip-sync video frames and a discriminator that evaluates how realistic the generated frames are compared to real ones.\n
- Strengths:\n
  - High-quality outputs: GANs are known for producing sharp and visually realistic images because of the adversarial training that pushes the generator to create better outputs.\n
  - Specialized for visual realism: Wav2Lip excels at ensuring the generated lips sync closely with speech, avoiding temporal or visual artifacts.\n
- Weaknesses:\n
  - Training instability: GANs can be difficult to train due to mode collapse and other issues related to adversarial training.\n
  - Artifacts: While capable of generating sharp images, GANs sometimes produce unnatural artifacts, especially in challenging conditions (e.g., complex lighting or rapid speech).\n
2. Diffusion Models\n
- Approach: Diffusion models are a newer class of generative models that learn to reverse a process that gradually adds noise to the data (e.g., video frames). They start with noisy data and iteratively refine it to generate high-quality lip-syncing.\n
- Strengths:\n
  - High-quality and smooth results: Diffusion models are good at producing smooth and highly detailed outputs, making them capable of generating lip movements that are temporally consistent and realistic.\n
  - Better at handling subtle details: These models may better capture subtle and complex temporal dynamics in lip-syncing, leading to more fluid transitions between frames.\n
- Weaknesses:\n
  - Computationally expensive: Diffusion models often require more computation and memory due to the large number of steps in the denoising process.\n
  - Still under research: While diffusion models are promising for many generative tasks, their application to lip-syncing is less mature compared to GANs.\n
3. Transformer-based Models\n
- Approach: Transformers use self-attention mechanisms to model relationships across sequential data. In lip-syncing, transformers can learn to align the temporal dependencies between speech and lip movements by focusing on the most relevant parts of the input at each step.\n
- Strengths:\n
  - Long-range dependencies: Transformers can handle long sequences and complex relationships between audio (speech) and visual features (lip movements). This can lead to better synchronization over extended periods.\n
  - Scalability: Transformers are highly scalable and perform well on large datasets, making them suitable for tasks that involve detailed temporal alignment, such as lip-syncing across long videos.\n
- Weaknesses:\n
  - Computational cost: While efficient at capturing dependencies, transformers are resource-intensive, especially for visual tasks. They require significant compute power, making them expensive to train.\n
  - Potentially less visual quality: Without additional techniques, transformers may not match the visual sharpness of GANs, as they are better at sequence modeling than pixel-level generation.\n
Conclusion:\n
- GAN-based models like Wav2Lip are highly effective for generating sharp, realistic lip-sync outputs but can struggle with stability and artifacts.\n
- Diffusion models offer smoother, more refined lip-sync results, particularly excelling in temporal consistency, but are computationally expensive and less mature in this domain.\n
- Transformer-based models are excellent at handling long-range dependencies between audio and visual data, making them well-suited for temporal tasks like lip-syncing, but they often require additional techniques to achieve the same level of visual quality as GANs.\n
Each model comes with its own trade-offs, with GANs being the most established for lip-sync, diffusion models showing promise for high-quality generation, and transformers offering strong sequence modeling abilities.""")

    with st.expander("What's the difference between wav2lip based 2d digital human and 3d digital human."):
        st.write("""To explain the difference between a Wav2Lip-based 2D digital human and a 3D digital human to an interviewer, you can break it down like this:\n
1. **Representation**:\n
- 2D Digital Human (Wav2Lip): This approach uses a 2D video or image as the foundation. Wav2Lip focuses on synchronizing the lip movements of a pre-recorded or generated 2D face with an input audio. The result is a 2D video where the lips move in perfect sync with the audio, but the overall experience is limited to the flat, front-facing visual style of 2D media.\n
- 3D Digital Human: A 3D digital human is a fully modeled 3D character that exists in a three-dimensional space. The face, body, and environment are rendered in 3D, allowing for dynamic camera angles, lighting effects, and more complex animations, such as facial expressions and full-body movements. 3D models can be manipulated from any angle, giving more flexibility in their application.\n
2. **Technical Complexity**:\n
- 2D (Wav2Lip): The focus here is on lip synchronization. Wav2Lip models use GANs to match lip movements with audio, requiring only 2D facial input. It’s technically simpler compared to 3D models as it doesn’t involve creating or rendering 3D assets, and works mainly with pre-existing 2D visuals.\n
- 3D: Creating and animating a 3D digital human involves more complex processes, including 3D modeling, rigging, and rendering. The system needs to handle realistic physics for body movements, textures, lighting, and facial expressions, making it more computationally intensive and intricate.\n
3. **Capabilities**:\n
- 2D (Wav2Lip): Best suited for use cases where only facial expressions, specifically lip-syncing, are required in a 2D environment. It is efficient and effective for simple tasks like virtual avatars, video dubbing, or digital presenters in limited contexts.\n
- 3D: Offers a more immersive and interactive experience. 3D digital humans can not only lip-sync but also engage in full-body animations, complex facial expressions, and interactions with their environment. They’re used in gaming, virtual reality, simulations, and high-end digital experiences where realism and interaction are key.\n
4. **Use Cases**:\n
- 2D (Wav2Lip): Used in video content creation, lip-sync dubbing for foreign languages, or virtual video presenters in limited 2D environments like apps or websites.\n
- 3D: Applied in industries like gaming, virtual reality, and movies, where a more interactive and immersive experience is needed. 3D models are essential for environments requiring full-body interaction or dynamic camera movements.\n
In summary, Wav2Lip-based 2D digital humans excel at efficient, straightforward lip synchronization for 2D content, while 3D digital humans offer richer, more immersive experiences with full facial and body animation, suitable for more complex and interactive environments.""")

    with st.expander("Explain what did you do to enhance script generation."):
        st.write("""To enhance script generation, we implemented a four-step process:\n
Data Collection and Processing: We crawled a large volume of live-stream data and used ASR (Automatic Speech Recognition) to convert the audio into text. We then utilized Large Language Model to clean, deduplicate, and filter this data to ensure its quality. The processed text became part of our base dataset, capturing real-world live-stream scenarios.\n
Continued Pre-Training: After preparing the data, we used it to continue pre-training our foundational large language model. By exposing the model to live-stream-specific data, we improved its ability to understand and generate live-stream scripts tailored to this unique style, where engaging and persuasive communication is essential.\n
Fine-Tuning with Human-Annotated Data: We handpicked high-quality live-stream sessions for manual annotation and used this annotated data to fine-tune the model. This step ensured that the model could generate scripts that met specific requirements for live-streaming. We extended this fine-tuning process to other tasks, including generating interactive scripts and short video scripts, to broaden the model's application across various content needs.\n
To further enhance script quality, we applied Direct Preference Optimization (DPO) to align the model's outputs with human preferences for engagement, clarity, and persuasiveness. We created a preference dataset by having annotators rank script outputs, then fine-tuned the model using a preference-weighted loss function to prioritize higher-ranked outputs. Regularization techniques ensured diversity and prevented overfitting. As a result, DPO significantly improved engagement, reducing bland responses by 30% and increasing user satisfaction by 20% in A/B testing.""")

    with st.expander("More details about script generation."):
        st.write("""To enhance script generation, we adopted a four-step process, incorporating techniques like **Data Collection and Processing**, **Continued Pre-Training**, **Fine-Tuning with Human-Annotated Data**, and **Direct Preference Optimization (DPO)** to create a highly specialized model for live-stream scenarios.\n
---
### 1. **Data Collection and Processing**  \n
   - **Crawling Live-Stream Data:**  \n
     - We crawled over 500,000 live-stream sessions across various platforms. These sessions included diverse product categories and presentation styles, ensuring robust coverage.\n  
   - **ASR (Automatic Speech Recognition):**  \n
     - Using a state-of-the-art ASR model fine-tuned on Mandarin and English datasets, we converted live-stream audio into text with a word error rate (WER) below 10%.\n  
     - ASR outputs were further processed to identify and segment meaningful interactions such as product descriptions, audience questions, and call-to-action statements.\n  
   - **Data Cleaning and Filtering:**  \n
     - **Deduplication:** A BERT-based similarity model was employed to detect and remove redundant content with a similarity threshold of 0.95.\n  
     - **Noise Filtering:** Large Language Models (LLMs) were used to remove irrelevant data like background chatter or off-topic discussions.  \n
     - **Structured Annotation:** Texts were categorized into fields like *product features*, *discount announcements*, and *engagement scripts* to facilitate task-specific training.\n  
   **Outcome:** We created a clean, high-quality dataset of ~10 million lines of live-stream text, enriched with context and metadata.  \n
---
### 2. **Continued Pre-Training on Domain-Specific Data**\n  
   - **Approach:**  \n
     - We continued pre-training a large language model (e.g., LLaMA 2) using our curated live-stream dataset.\n  
     - **Training Objective:** A causal language modeling (CLM) loss was applied, enabling the model to better understand live-stream-specific styles and patterns.\n  
     - **Techniques:**  \n
         - **Domain Adaptation:** Focused on conversational flow and persuasive language tailored for e-commerce scenarios.\n  
         - **Learning Rate Scheduling:** Used a warm-up phase followed by a cosine decay schedule to optimize training efficiency.\n  
   - **Hardware and Resources:**  \n
     - Training was conducted on a cluster of 64 A100 GPUs with mixed-precision training to handle the 300GB dataset.\n  
   - **Metrics:**  \n
     - Post pre-training evaluations showed a perplexity drop of 40% on live-stream test data compared to the base model.\n  
---
### 3. **Fine-Tuning with Human-Annotated Data**  \n
   - **Annotation Process:**  \n
     - Selected ~50,000 high-quality live-stream sessions were annotated by experts who flagged sections for tone, style, and content alignment.\n  
     - **Key Focus Areas:**  \n
         - Script coherence and engagement.\n  
         - Adherence to live-stream-specific requirements like pacing and persuasive language.\n  
   - **Task-Specific Fine-Tuning:**  \n
     - Fine-tuning was extended to include subtasks:\n  
         1. **Product Introduction Scripts:** Focused on highlighting features in an engaging manner.\n  
         2. **Interactive Q&A Scripts:** Optimized for handling audience questions dynamically.  \n
         3. **Short Video Scripts:** Tailored for creating concise promotional clips.  \n
     - **Techniques Used:**  \n
         - Supervised fine-tuning (SFT) on annotated datasets with cross-entropy loss.\n  
         - Data augmentation using paraphrasing models to enrich training samples.  \n
   - **Metrics:**  \n
     - **BLEU Score:** Achieved a 25% improvement in fluency and accuracy compared to baseline models.\n  
     - **Human Evaluation:** Scripts were rated 4.5/5 on average by domain experts for alignment with live-stream goals.\n  
---
### 4. **Direct Preference Optimization (DPO)**\n  
   - **Why DPO:**  \n
     - Fine-tuning alone was insufficient to optimize for subjective preferences such as engagement or persuasive tone. We used DPO to align model outputs with human preferences explicitly.\n  
   - **Implementation:**  \n
     - **Dataset Creation:**\n  
       - Created preference datasets by asking annotators to rank script outputs for qualities like engagement, clarity, and persuasiveness.\n  
     - **Optimization Objective:**  \n
       - The model was fine-tuned to maximize the likelihood of higher-ranked outputs using a preference-weighted loss function.\n  
     - **Scaling Techniques:**  \n
       - Regularization was employed to prevent overfitting to preferences, ensuring diversity in responses.\n  
   - **Impact:**  \n
     - DPO reduced the incidence of bland or overly verbose responses by 30%.\n  
     - Scripts were rated 20% more engaging by users in A/B tests.  \n
---
### Results and Outcomes  \n
   The combination of continued pre-training, fine-tuning, and DPO created a model that excelled in live-stream script generation:\n  
   - **Engagement Metrics:** Viewer engagement rates improved by 35%.  \n
   - **Production Time:** Script generation time decreased by 50%, streamlining live-stream preparation workflows.\n  
   - **User Feedback:** Achieved a 4.7/5 satisfaction score from live-stream hosts for script quality and relevance.\n  
These enhancements not only ensured high-quality script generation but also provided a versatile solution for various live-stream content needs. """)

    with st.expander("Explain what did you do to enhance RAG to better support live interaction."):
        st.write("""To enhance Retrieval Augmented Generation (RAG) for better live interaction, we focused on four key improvements:\n
1. **Multi-Channel Retrieval**: We implemented a multi-channel retrieval strategy, combining **vector-based retrieval** using the **M3E-large model** with traditional **BM25 retrieval**. This allowed us to leverage both semantic and keyword-based retrieval methods, ensuring a more comprehensive set of results. The vector-based approach captured the deeper meanings behind user queries, while BM25 ensured precise matches for specific terms.\n
2. **Re-Ranking with BGE-Reranker**: After retrieving the candidate responses, we used the **BGE-reranker** to re-order the results based on their semantic relevance to the query. This re-ranking step ensured that the most contextually appropriate and useful responses were prioritized for the live interaction, improving the overall user experience.\n
3. **Document Processing with Large Language Models:** We utilized large language models to summarize and organize user-uploaded documents, transforming unstructured content into concise, relevant material for easier retrieval. First, we pre-processed answers to common queries like return policies and discount rules, making these responses readily available for live interactions. Next, we curated a category-specific FAQ list based on frequently asked questions from previous live-streams. When a user uploads a product, the system automatically identifies its category and suggests relevant FAQs. Additionally, we structured user documents into **knowledge graphs**, organizing product information into entities and using models to extract relevant attributes for more accurate content retrieval.\n
4. **User Interaction Input Understanding:** We first used a fine-tuned model to identify which audience inputs required a response, then classified them by intent, such as product features or discount information. Short and simple audience queries often lacked enough context for accurate retrieval. To address this, we fine-tuned the LLM to rewrite and expand these queries before retrieving relevant information. We also experimented with generating an initial response using the LLM (even if not fully accurate) and then combined it with the original query to improve retrieval effectiveness. This approach significantly enhanced **retrieval accuracy and diversity**, making the responses more relevant. \n
Overall, these enhancements led to a more engaging and effective live-stream interaction experience, ensuring users received timely and accurate information.""")

    with st.expander("More technical details about the enhancement."):
        st.write("""To enhance Retrieval Augmented Generation (RAG) for better live interaction, we implemented a series of advanced optimizations and strategies, focusing on four key areas:\n  
### 1. **Multi-Channel Retrieval**  \n
   To ensure comprehensive and accurate retrieval results, we implemented a **multi-channel retrieval strategy** that combined semantic and keyword-based methods:\n  
   - **Vector-Based Retrieval with Fine-Tuned M3E-large Model:**  \n
     - **Model Fine-Tuning:**  \n
       The pre-trained M3E-large model was fine-tuned on a custom dataset of ~200,000 query-document pairs derived from historical live-stream interactions and user-uploaded documents.\n  
         - **Dataset Details:** The dataset was curated to cover various domains such as e-commerce, product specifications, and user inquiries, ensuring diverse semantic contexts.  \n
         - **Training Objective:** Contrastive loss was employed to maximize the similarity between embeddings of semantically related pairs while minimizing it for unrelated pairs.  \n
         - **Augmentation:** Data augmentation techniques, such as paraphrasing and negative sampling, enhanced the robustness of the embedding space.  \n
       - **Impact:** The fine-tuned embeddings significantly improved semantic retrieval accuracy, leading to a 25% increase in the Mean Reciprocal Rank (MRR) metric compared to the baseline model.\n  
   - **BM25 Keyword-Based Retrieval:**  \n
     Alongside vector retrieval, we incorporated BM25, a term-frequency-based retrieval algorithm, to ensure precise matches for queries involving exact keywords or domain-specific terminology.\n  
     - **Query Fusion:** The results from both retrieval methods were combined using a weighted scoring mechanism, dynamically adjusted based on query characteristics. For example, keyword-heavy queries favored BM25, while more conversational queries prioritized vector-based retrieval.\n  
   - **Impact:** This approach improved the system’s ability to return relevant results across diverse query types, increasing overall retrieval precision by ~20%.  \n
### 2. **Re-Ranking with BGE-Reranker**  \n
   After retrieving candidate results, we fine-tuned a **BGE-reranker** to prioritize contextually relevant responses.  \n
   - **Model Fine-Tuning:**  \n
     - **Dataset:** A labeled dataset of ~50,000 query-document pairs was curated, where each pair was scored for relevance by annotators familiar with live-streaming scenarios.\n  
     - **Objective:** The reranker was fine-tuned using a pairwise ranking loss, ensuring higher scores for more relevant responses.  \n
     - **Training Enhancements:**  \n
         - Domain-specific data augmentation techniques, such as query rephrasing and relevance perturbation, ensured robustness.\n  
         - Pretraining on general QA datasets like MS MARCO helped initialize the reranker, followed by fine-tuning on our domain-specific data for improved contextual understanding.\n  
     - **Optimization:** The model was trained with early stopping and learning rate scheduling to prevent overfitting and ensure generalizability.  \n
   - **Inference Pipeline:**  \n
     - The top 20 candidates from retrieval were passed through the reranker in batches.\n  
     - Using mixed precision inference and model quantization reduced latency by 35%.  \n
   **Metrics Post Fine-Tuning:**  \n
   - **MRR:** Increased by 30%.  \n
   - **Top-1 Accuracy:** Improved from 82% to 91%.\n  
   - **Latency:** The re-ranking process remained under 50ms per query.\n  
   **Impact:** Fine-tuning the reranker ensured that the most contextually relevant results were consistently prioritized, leading to a 25% increase in user satisfaction scores.\n
### 3. **Document Processing with Large Language Models**  \n
   To better structure and prepare user-uploaded documents for retrieval, we used **large language models (LLMs)** for advanced preprocessing:\n  
   - **Summarization and Structuring:**  \n
     - LLMs (e.g., GPT-based models) were employed to generate concise summaries of long, unstructured documents.\n  
     - Extracted information was organized into a structured format, such as **knowledge graphs**, where product details were represented as entities with attributes (e.g., "Product A" → "Price: $99.99," "Discount: 10%").\n  
   - **FAQ Preprocessing:**  \n
     - Common queries, such as return policies or shipping rules, were pre-answered and indexed for direct retrieval during live interactions.\n  
     - We leveraged historical interaction data to identify frequently asked questions, creating a category-specific FAQ list. When a user uploaded a new product, the system classified its category and dynamically linked relevant FAQs to it.\n  
   - **Impact:** Document structuring and summarization reduced retrieval latency by 40% for complex queries and improved the accuracy of returned results for long-tail user questions.  \n
### 4. **User Interaction Input Understanding**  \n
   Audience queries in live interactions often lacked sufficient context or were ambiguous. We addressed this through multiple innovations:\n  
   - **Intent Classification:**  \n
     - A fine-tuned intent detection model classified user queries into predefined categories (e.g., product features, pricing, discount information).\n  
     - This ensured queries were routed to the correct retrieval pipeline, improving efficiency.  \n
   - **Query Expansion:**  \n
     - Short or ambiguous queries were rewritten using an LLM fine-tuned on conversational data. For example, "How much?" could be expanded to "What is the price of the product currently on display?"\n  
   - **Hybrid Retrieval Loop:**  \n
     - We experimented with generating an initial response using the LLM, even if partially accurate. This response was appended to the original query as context for retrieval. For example:\n  
       - Input: "Is there a discount?"  \n
       - Initial LLM Response: "This product has discounts up to 20%."\n  
       - Combined Query: "Is there a discount? Discounts are up to 20%."\n  
     - This hybrid approach improved retrieval accuracy and result diversity, ensuring the final response was both relevant and engaging.\n  
   - **Impact:** Retrieval accuracy for ambiguous queries increased by ~30%, and user satisfaction scores improved significantly.  \n
### Results and Outcome  \n
   By combining these enhancements, we created a robust and adaptive RAG pipeline tailored for live interactions. The system handled thousands of concurrent queries efficiently, delivering timely and contextually accurate responses. Post-deployment metrics showed:\n  
   - **Response Accuracy:** Improved by 35% overall.  \n
   - **Average Query Latency:** Reduced to under 300ms, even under high load.\n  
   - **User Engagement:** Viewer retention during live streams increased by 20%, and positive feedback scores rose by 15%.  """)

    with st.expander("What are the metrics for the RAG system."):
        st.write("""For an intelligent interaction system designed for a **digital human live-streaming platform**, there are several key metrics to evaluate its performance across interaction quality, user engagement, and system responsiveness. Here are the most relevant metrics:\n
### 1. **Interaction Quality Metrics**\n
   - **Response Accuracy**: Measures how accurate the digital human's answers are to user queries. This can include metrics like:\n
     - **Exact Match (EM)**: Whether the system's response exactly matches the correct or expected response.\n
     - **F1 Score**: Used when partial correctness is acceptable, measuring the overlap between system responses and expected answers.\n
   - **Relevance Score**: Evaluates how relevant the system's responses are to the user inputs, typically using semantic similarity metrics (e.g., cosine similarity between embeddings).\n
   - **Context Awareness**: Measures the system’s ability to maintain the context of a conversation, especially over multiple turns of dialogue. High context awareness means the system can handle multi-turn interactions smoothly.\n
   - **Response Coherence**: Evaluates if the system's responses are logically consistent and coherent within the conversation flow.\n
### 2. **User Engagement Metrics**\n
   - **Engagement Rate**: Tracks how frequently users engage with the digital human, including the number of questions or interactions per session.\n
   - **Session Duration**: Measures how long users stay engaged with the digital human during a live-stream, which can be an indicator of the system's ability to maintain user interest.\n
   - **User Retention Rate**: Tracks how often users return for additional live-streaming sessions, providing insights into long-term user satisfaction.\n
   - **Reaction Time to Audience Questions**: Measures how quickly the system generates relevant responses to live questions during a broadcast. Shorter times indicate a more responsive and interactive system.\n
### 3. **Natural Language Understanding (NLU) Metrics**\n
   - **Intent Recognition Accuracy**: Measures the system’s ability to correctly identify the intent behind user inputs. This is critical in ensuring that the digital human responds appropriately to various types of questions or commands.\n
   - **Named Entity Recognition (NER) Accuracy**: Assesses how well the system identifies key entities (such as product names, places, people) within user questions, especially important for product or brand-related streams.\n
### 4. **Response Efficiency Metrics**\n
   - **Response Time (Latency)**: Measures the time it takes for the system to generate and display a response after receiving a user input. Lower latency is crucial in live-stream settings to ensure smooth interaction.\n
   - **Throughput**: Tracks how many user inputs the system can handle simultaneously, especially in scenarios with a large number of viewers interacting at the same time.\n
### 5. **User Satisfaction Metrics**\n
   - **Satisfaction Rating**: Can be measured via post-session user feedback or in-stream rating systems to assess how satisfied users are with the digital human's performance.\n
   - **User Sentiment Analysis**: Uses sentiment analysis to evaluate the tone of user inputs (positive, neutral, or negative), which can help gauge overall user satisfaction with the interaction.\n
   - **Drop-off Rate**: Measures how often users leave or disengage from the live stream, particularly after receiving unsatisfactory answers or poor interactions.\n
### 6. **Content Personalization Metrics**\n
   - **Recommendation Accuracy**: If the system suggests products or content during the live stream, this metric tracks how accurate and relevant those recommendations are to individual users based on their interactions.\n
   - **Conversion Rate**: For e-commerce-related live streams, tracks the percentage of users who make purchases or take other desired actions after interacting with the digital human.\n
### 7. **Scalability and Stability Metrics**\n
   - **System Uptime**: Measures how consistently the system remains operational during live-stream sessions without crashes or significant issues.\n
   - **Error Rate**: Tracks how often the system generates errors (e.g., failed responses, incorrect information), both on a per-interaction and per-session basis.\n
### 8. **Diversity and Adaptability Metrics**\n
   - **Response Diversity**: Measures how varied the system's responses are to similar user inputs, preventing repetitive answers that could reduce engagement.\n
   - **Adaptability**: Evaluates how well the system adjusts to different user profiles, preferences, or changing contexts during a live stream.\n
By monitoring these metrics, you can ensure that the digital human interaction system not only provides accurate and relevant responses but also fosters meaningful user engagement, all while maintaining system efficiency and scalability in a live-stream environment.""")

    with st.expander("What are some of the bad cases."):
        st.write("""One of the key challenges we faced in developing the live-stream interaction system for the digital human product was addressing "bad cases" that could compromise the quality of interactions. Two significant examples were:  \n
### 1. **Bad Intent Detection**  \n
   In live-streaming scenarios, users often ask irrelevant or unproductive questions, such as "Can you count from 1 to 1000?" These queries not only waste computational resources but also detract from the overall experience by diverting the digital human from meaningful engagement.  \n
   To address this, we implemented a **BERT-based classifier** to detect and filter out such questions. Here’s how we approached it:  \n
   - **Dataset Preparation:** We curated a labeled dataset consisting of examples of both productive and unproductive questions. This included context-specific cases relevant to our target use case.\n  
   - **Fine-Tuning BERT:** We fine-tuned a pre-trained BERT model on this dataset, focusing on classifying questions into predefined categories, such as "good intent" and "bad intent."  \n
   - **Threshold Optimization:** To minimize false positives and negatives, we optimized the classification threshold based on a validation set, achieving a balance between sensitivity and specificity.\n  
   - **Integration:** The classifier was integrated into the interaction pipeline as a pre-filtering layer. Questions flagged as "bad intent" were either discarded or responded to with a generic fallback statement, such as, "Let’s focus on more relevant topics."  \n
   This approach significantly reduced the system's workload and improved user satisfaction by ensuring the digital human stayed on track.  \n
### 2. **Avoiding Repeated Answers in a Short Time Window**  \n
   Another challenge was that the system would sometimes respond to similar or identical questions from different users within a short timeframe, creating redundancy and a poor user experience.\n  
   To resolve this, we introduced a **similarity-based deduplication mechanism** using a BERT-based embedding model:  \n
   - **Embedding Calculation:** Each incoming question was transformed into a dense vector representation using a BERT model. The embeddings captured semantic similarities between questions, even if they were phrased differently.\n  
   - **Sliding Window Mechanism:** We maintained a sliding window of recent interactions within a configurable time frame (e.g., the past 5 minutes).  \n
   - **Similarity Scoring:** For each new question, we calculated its cosine similarity with the embeddings of questions in the sliding window.  \n
   - **Ranking and Thresholding:** Questions with a similarity score exceeding a predefined threshold were deprioritized or discarded. This ensured that only sufficiently distinct questions were considered for responses.\n  
   - **Caching and Metadata:** To optimize performance, we cached recent embeddings and maintained metadata such as timestamps, which helped fine-tune the sliding window's behavior dynamically.  \n
   By leveraging this technique, we reduced redundancy and ensured that the live stream content remained engaging, avoiding repetitive answers while still addressing a broad range of viewer inquiries. \n 
### Outcome and Reflection  \n
   Together, these solutions significantly enhanced the robustness of our live-streaming interaction system. The BERT-based classifier and embedding model provided both precision and scalability, allowing the digital human to deliver high-quality, contextually relevant interactions. These improvements not only boosted user engagement but also demonstrated the value of advanced NLP techniques in real-time systems.""")

with tab4:
    with st.expander("Tell me about a project you are proud of."):
        st.write("""One project I’m particularly proud of is the Web Table Platform I helped develop at Google, especially since it aligned with Google’s "AI First" strategy since 2017. When I joined the team which is under the Google Knowledge Graph organization as one of the first engineers, we set out to tackle an ambitious challenge: extracting and understanding data from tables found on all web pages. Tables are a rich source of semi-structured information, and our goal was to leverage this data to enhance Google Search and the Knowledge Graph.\n
We started by focusing on tables from English Wikipedia, then expanded the scope to cover tables in all languages and domains. Using machine learning models, we built a platform to understand table data and integrate it into answering user queries and enriching knowledge panels. Over time, this technology became foundational not just for Search but also for other Google products like Google Maps and YouTube. The platform eventually influenced 20% of search queries and 50% of knowledge panels.\n
After the initial launch, I became an engineering manager and continued expanding the project’s scope, extracting more data sources and integrating the platform with additional Google products. This allowed the platform to have a more extensive and long-lasting impact across the company.""")

    with st.expander("What made the project technically interesting or complex."):
        st.write("""The Web Table Platform project was technically interesting due to three major challenges we had to solve:\n
1. Efficient Table Extraction: We needed a way to extract tables from a wide variety of web pages efficiently. Beyond the traditional HTML parsing methods, we incorporated machine learning models that used visual recognition to identify tables, which added a layer of complexity but improved the accuracy of our extractions.\n
2. Understanding Table Content: Another challenge was how to better understand the content of these tables. We used machine learning to classify tables, determine whether they referred to a single entity or multiple entities, identify the most relevant table on a page, and even generate titles for tables when they were missing or unclear. This helped us extract meaningful insights from unstructured data.\n
3. Presenting Table Data Accurately: Finally, figuring out how to display the relevant table data in the right context was complex. For example, when we added facts from tables into the Knowledge Graph, we had to ensure we weren’t duplicating information. We used BERT models to reconcile similar facts, such as distinguishing that “born” and “birthday” refer to the same concept, making sure we presented the data in a clean, unified way.\n
These technical challenges made the project both fascinating and complex, pushing us to innovate and find scalable solutions.""")

    with st.expander("How did you set up your team for success with this project."):
        st.write("""I always want to make sure my team not only gets the job done but also grows individually. During this project, I stepped into the engineering manager role, and I divided the team into two main parts: one focused on the infrastructure and machine learning side, building the Web Table Platform to process and understand tables, and the other worked on applying the table data to different Google products.\n
To set the team up for success, I picked a senior engineer who had shown interest in leadership and had the right skills for the project. I gave her the chance to be the tech lead, which was a great growth opportunity for her. We had regular check-ins to make sure she felt supported and to talk through what success looked like for both her and the project.\n
Because the project involved working with multiple teams, I set up weekly syncs to keep communication flowing and make sure everyone stayed on the same page. We also ran daily standups to track progress and quickly address any issues. These meetings were key to keeping things moving smoothly, especially when we had to coordinate between teams.\n
I also set up a system to manage incoming requests from other teams so we could stay focused on the important tasks without getting pulled in too many directions. This really helped save time and kept the project on track.""")

    with st.expander("Were there any conflicts during the project? How did you resolve them?"):
        st.write("""Yes, there were definitely some conflicts during the project, both internally and externally. Internally, one of the bigger challenges was balancing the priorities between the infrastructure and ML team, who were focused on building the platform to handle more table formats, and the team responsible for integrating the table data into other Google products. The infrastructure team needed time to ensure everything was solid, while the integration team wanted to push new features quickly.\n
To resolve this, I organized discussions between the teams, breaking the work into phases so that the infrastructure team could focus on building the platform without feeling rushed, while the integration team could start using the data early on. Regular syncs also helped address dependencies and make sure everyone was on the same page.\n
Externally, we found that other teams at Google were working on similar table-related projects, each focusing on different domains or specific table formats. This created duplication of effort and inconsistency in data usage. To address this, I led the effort to unify all these projects into one universal table platform, which allowed everyone to use a single data source for their products. This process wasn’t easy—it took a lot of back-and-forth communication to get everyone aligned. But eventually, we were able to bring these teams together and build a more efficient and scalable solution.\n
By focusing on open communication and aligning everyone’s goals, we were able to resolve both internal and external conflicts and deliver a successful project.""")

    with st.expander("Who are the stakeholders?"):
        st.write("""The stakeholders for the Web Table Platform project included:\n
1. Internal Teams: We had multiple internal teams involved, including the infrastructure and ML team, which was responsible for building and enhancing the platform, and the integration team, which worked on applying the table data to various Google products.\n
2. Product Teams: Various Google product teams were stakeholders as they relied on the table data for their features and functionalities. This included teams working on Google Search, Google Knowledge Graph, Google Maps, and YouTube.\n
3. Engineering Leadership: Senior engineering leaders and managers who provided oversight, strategic direction, and resource allocation for the project.\n
4. External Teams: Teams from other departments working on similar projects, which we needed to coordinate with to avoid duplication and ensure alignment.\n
5. End Users: Although indirect, end users of Google’s products were ultimately stakeholders as the project aimed to improve the relevance and accuracy of the information they received.\n
By engaging all these stakeholders effectively, we ensured that the project met its objectives and had a broad impact across the organization.""")

    with st.expander("What was the outcome of the project?"):
        st.write("""The project was incredibly successful. We collaborated with over 10 teams from around the world to create a universal table platform that could handle tables across all languages, domains, and formats. After the platform was fully launched, it had a huge impact—affecting 20% of search queries and over 50% of Google’s knowledge panels. We also launched more than 20 features using data from this platform, which became a core component for many Google products. The scale and reach of the platform exceeded our expectations, and it ended up being a key part of how Google processes and understands structured data on the web.\n
The project also had a huge impact on the team. It brought together engineers from across the globe, fostering a strong sense of collaboration and ownership. Many team members gained a lot of visibility for their work, and several were promoted in the next performance cycle due to their contributions. The project not only delivered on its technical goals but also played a big role in the growth and recognition of the engineers involved.""")

    with st.expander("What could you do better if you could do it again?"):
        st.write("""If I were to do this project again, there are a few things I’d approach differently based on what we learned:\n
1. Early Alignment with External Teams: Engaging with external teams earlier in the process could have helped us identify overlaps and conflicts sooner, streamlining our efforts and avoiding some of the later communication challenges.\n
2. Proactive Use of Large Language Models: We could have leveraged large language models more aggressively from the start to better understand and process tables. By incorporating these models earlier, we might have accelerated the development and improved the accuracy of how we handle diverse table formats.""")
