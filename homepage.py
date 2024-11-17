import streamlit as st

st.title("Behavior questions")

tab1, tab2, tab3, tab4 = st.tabs(["Introduction", "Management Skills", "Digital Avatar", "Web Table"])
with tab1:
    with st.expander("Introduction."):
        st.write("""Hello, I’m Hongjun. I have over ten years of experience in the software engineering industry, specializing in machine learning and large-scale system architecture. Currently, I’m working at CloudWalk Technology in Shanghai, where I lead teams in developing AI products. My work includes developing LLM-based Knowledge Engines, as well as creating an AIGC product that integrates digital avatar and LLM for video creation and e-commerce live streaming.\n
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
After I joined CloudWalk, I continued leading the Knowledge Engine team. My team developed two key products: one was a knowledge engine based on large language models, and the other was an AIGC platform that integrated these models with digital avatars. The knowledge engine extracts information from documents to build knowledge graphs, which are then used to enhance retrieval augumented generation (RAG). On the AIGC platform, we helped users create e-commerce live-streaming scripts and dialogues, and enabled real-time interactions with viewers through large language models. To ensure our products performed well, we carried out extensive data processing and fine-tuned the models using machine learning techniques.""")

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
    with st.expander(""):
        st.write("""""")

    with st.expander(""):
        st.write("""""")

    with st.expander(""):
        st.write("""""")

with tab2:
    st.header("Meta specific questions")
    with st.expander("Why do you want to join Meta?"):
        st.write("""I’m excited about the opportunity at Meta because it’s at the forefront of innovation in AI and machine learning, driving advancements that impact billions of users globally. Meta’s work in areas like recommendation systems, augmented reality, and large-scale AI models aligns perfectly with my experience and passion for building impactful machine learning products.\n
One aspect that particularly excites me is Meta’s commitment to openness and collaboration in AI. By open-sourcing models like Llama, Meta is empowering the global AI community to innovate and build on top of its cutting-edge work. In many ways, Meta has become the “real OpenAI,” fostering accessibility and transparency while advancing the boundaries of AI research.\n
As a Machine Learning Engineering Manager, I’m eager to contribute to projects that shape the future of social interaction and digital experiences. Meta’s mission of connecting people and pushing the boundaries of technology resonates with me, and I’m excited about the chance to lead teams that will make a meaningful difference in that vision.""")

    with st.expander("What questions do you have for me?"):
        st.write("""Company Culture and Values:\n
- "Can you describe the company culture and what it’s like to work here day-to-day?"\n
- "How does the company support professional development and career growth?"\n
Role and Expectations:\n
- "What are the key challenges and opportunities for this role in the first six months?"\n
- "How do you measure success in this position, and what are the primary goals for the person in this role?"\n
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
2. Timeliness: I give feedback as close to the event as possible, whether it’s positive or developmental, so it’s relevant and actionable.  \n
3. Balance: I ensure a balance of positive reinforcement and areas for improvement. Highlighting what’s working well keeps morale high, while constructive feedback fosters growth.\n  
4. Collaborative Approach: I frame feedback as a dialogue. For instance, I might ask, “How do you think this approach worked? Is there something we could adjust?” to encourage self-reflection and mutual problem-solving.\n  
Receiving Feedback:\n
1. Be Open-Minded: I view feedback as an opportunity to learn and improve. Even when the feedback is unexpected or challenging, I focus on understanding the perspective rather than reacting defensively.\n  
2. Seek Clarity: I ask clarifying questions to ensure I understand the feedback fully, such as, “Can you provide an example so I can better address this?”  \n
3. Take Action: I prioritize acting on feedback and communicating my progress. For instance, when I received feedback about improving communication with external stakeholders, I implemented more structured updates and sought further feedback on their effectiveness.\n  
4. Create a Feedback Loop: I encourage my team and peers to provide regular feedback. This builds a culture of trust and continuous improvement.  \n
At Meta, where feedback is integral, my approach would align well with fostering a collaborative and growth-oriented team environment.""")

    with st.expander("If you have unlimited resources, what feature do you want to implement for meta?"):
        st.write("""If I had unlimited resources, I would build a Knowledge-Powered AI Assistant with Long-Term Memory and Personalization that seamlessly integrates across Meta’s platforms. This agent would leverage advancements in generative AI, multimodal interactions, and cross-platform integration, while drawing from my expertise in search, knowledge graphs, and digital human technologies.\n  
Feature Overview:\n
The AI assistant would act as a highly personalized digital companion, capable of assisting users in a wide range of tasks:\n  
1. Long-Term Memory: The agent would retain contextual knowledge about users over months or years, enabling it to evolve with their needs. For example, it could remember a user’s interests, past interactions, and ongoing goals, offering tailored recommendations and insights.\n  
2. Personalization: Using advanced AI and knowledge graph technologies, the agent would dynamically adapt to users’ preferences, whether it’s curating content, facilitating social connections, or assisting with productivity tasks.  \n
3. Knowledge-Powered Intelligence: With a robust foundation in search and structured data from knowledge graphs, the agent would provide accurate and actionable responses, acting as both a conversational partner and a reliable information source.\n  
4. Generative and Multimodal Interaction: The agent would support text, voice, video, and even digital avatar-based communication, ensuring a seamless and immersive experience across Meta’s platforms (Facebook, Instagram, WhatsApp, Horizon, etc.). \n 
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

    st.header("Conflicts and other challenges")
    with st.expander("Tell me about a time you had to mediate a conflict inside your team."):
        st.write("""While working on the digital human product, a conflict arose between our frontend and backend engineers. The frontend engineer proposed directly integrating the LLM API to simplify the process and quickly show results. The backend engineer, however, insisted that all API calls should be routed through the backend, just like the other APIs, to maintain consistency and control.\n
As the engineering manager, I facilitated a discussion to understand both perspectives. The frontend engineer was focused on the simplicity and speed of directly integrating the API, while the backend engineer was concerned about scalability and long-term maintainability. After assessing the technical implications, we realized that if the frontend handled the API calls, we wouldn't be able to track user behavior effectively. This would hinder our ability to improve the LLM's performance based on user feedback.\n
In the end, we decided to route the LLM API calls through the backend to ensure better scalability, user tracking, and overall consistency with our system architecture. This resolution aligned both teams and ensured long-term flexibility for improving the product.""")
    with st.expander("Tell me about a time you resolved a conflict between an engineer on your team and a cross-functional partner. "):
        st.write("""While working on the digital human product at CloudWalk, a conflict arose between our backend architect and an engineer from the infrastructure team. The backend architect believed we needed a new resource scheduling system to support the unique requirements of digital human rendering for a consumer-facing product. The infrastructure engineer, however, felt that the existing system, designed for B2B projects, could be adapted with minor adjustments rather than a full overhaul.\n
As the engineering manager, I stepped in to mediate. First, I met with both engineers individually to understand their concerns. The backend architect was focused on the need to scale for potential explosive user growth, while the infrastructure engineer wanted to avoid unnecessary complexity and costs.\n
To move forward, I also met with the manager of the infrastructure team. Together, we estimated the required resources, task complexity, and the timeline for either approach. After a thorough assessment, we agreed that redesigning the resource scheduling system was the best long-term solution for scalability and performance. We adjusted the project scope to accommodate the changes, ensuring that both teams had the resources and time needed.\n
By fostering open communication and collaborating with the infrastructure manager, we reached a solution that balanced immediate technical needs with future scalability, turning the conflict into an opportunity to build a more robust system.""")

    with st.expander("Tell me about a time you had conflicts with other team."):
        st.write("""During the development of our digital human product, there was a debate between teams about whether we should focus more on 2D or 3D digital humans. The machine learning team had been splitting resources almost equally between the two, believing that 3D would offer more advanced capabilities, such as a higher level of realism and interactivity. However, 3D models required more complex computations and expensive hardware for rendering, making them resource-intensive and time-consuming to develop. On the other hand, 2D digital humans, based on video or images, focused primarily on lip synchronization, which made them much more efficient and technically simpler. This allowed them to be produced faster and at a lower cost, making them more practical for the immediate needs of our users.\n
After conducting market research, we found that e-commerce professionals preferred 2D digital humans because they appear more realistic, as they are derived from real video footage. Although 3D digital humans have a more high-tech and dynamic appearance, it’s pretty clear right away that they aren’t real, which made them less ideal for e-commerce live-streaming.\n
I stepped in to mediate by conducting a thorough analysis of user feedback and market trends. It became clear that 2D digital humans aligned better with what our users actually wanted in the short term and would allow us to deliver value faster with fewer resource constraints. I presented this data-backed analysis to senior management and external teams, explaining that focusing on 2D would lead to a quicker, more successful product launch, while we could still explore 3D in the future as the market evolved.\n
By keeping communication open and providing a clear comparison of the pros and cons of each approach, I was able to convince the external teams to reallocate resources towards 2D digital humans. This decision helped the project stay focused and contributed to its overall success in the market.""")
    with st.expander("What areas do you seek for growth? "):
        st.write("""I'm always seeking opportunities to grow both :blue-background[technically and as a leader].\n
On the leadership side, I want to further enhance my ability to coach and mentor engineers, helping them reach their full potential. While I have experience managing teams, I'm particularly focused on refining my skills in aligning individual goals with broader company objectives and fostering a collaborative environment that drives innovation.\n
Technically, I'm especially excited about advancing my expertise in Large Language Models (LLMs). With the rapid developments in this field, I see significant potential in pushing the boundaries of LLMs, particularly in fine-tuning them for specific tasks, improving the efficiency of model training and inference, and exploring how LLMs can be leveraged to build intelligent systems that better understand context, reason with data, and generate human-like responses.\n
Additionally, I'm focused on improving my communication with non-technical stakeholders to ensure that the business impact of ML projects is clear and aligns with the company's strategic objectives.""")

    with st.expander("Describe your failure. How did you conquer it?"):
        st.write("""One significant failure I encountered was during a project at CloudWalk for a government client, where we needed to develop a new feature for our knowledge engine to extract information from policy documents. We initially based our planning on sample documents provided, but the actual documents proved to be much more complex. They included a variety of formats, such as handwritten scans, which made accurate understanding and processing challenging.\n
I underestimated the complexity of integrating this new feature with our existing systems. Consequently, we missed our launch deadline, which affected the team’s morale and delayed other projects.\n
To address the issue, I led a thorough reassessment of the project requirements and identified gaps in our initial planning. We revised our approach by enhancing our model training processes to accommodate the diverse document formats and placing greater emphasis on risk management and regular progress reviews.\n
Ultimately, we successfully delivered the feature with a revised timeline, and it was well-received by the client. This experience highlighted the importance of thorough initial assessments and proactive risk management, and reinforced the need for flexibility and frequent updates in project planning to achieve successful outcomes.""")

    with st.expander("What's your weakness?"):
        st.write("""One area where I’ve historically been less experienced is actively promoting a product to the public or directly advertising it. While I’m confident in communicating with internal stakeholders and business-side teams, my exposure to public-facing marketing and consumer outreach has been more limited.\n  
However, I’ve taken steps to address this. For instance, during my time at CloudWalk working on the digital human product, I collaborated closely with the marketing team to better understand how to position the product for consumers. I also participated in client-facing presentations to gather feedback and refine the product's messaging based on their needs. These experiences helped me build a stronger connection between product development and market expectations.\n  
I’m eager to grow further in this area by learning from experts in marketing and public relations, leveraging data-driven insights to shape consumer messaging, and participating more directly in public-facing engagements. I view this as an opportunity to enhance my ability to connect technical solutions with broader market impact.""")

    with st.expander("Describe a situation where you adapted to change / have to pivot during development."):
        st.write("""I adapt to change by staying :blue-background[flexible and open-minded], while focusing on continuous learning and maintaining clear communication. In dynamic environments, I actively seek to understand the reasons behind the change and quickly adjust my priorities accordingly.\n
For example, when our company shifted its strategy to focus more on large language model (LLM) applications after the release of ChatGPT, I conducted thorough research to understand the new landscape and identified a market opportunity in digital human technology. Despite this being a major change in direction, I successfully led the development of a new product that became a core offering and generated significant revenue for the company.\n
I’ve learned that the key to adapting well is staying proactive, communicating regularly with stakeholders, and ensuring that I align my actions with the evolving business goals. By staying resilient and open to feedback, I’m able to turn changes into opportunities for growth and innovation.""")

    with st.expander("What was some difficult feedback that you received? and why was it hard to receive?"):
        st.write("""One of the most difficult pieces of feedback I received was when I was promoted to engineering manager for the first time at Google. A colleague pointed out that I wasn’t giving enough autonomy to my team. I tended to get too involved in the details, especially when we were under tight deadlines. At the time, I thought I was helping, but the team felt micromanaged and less empowered to make decisions.\n
This feedback was hard to accept because I saw myself as a supportive leader, and it challenged my perception of my leadership style. Initially, I felt defensive, as I believed I was just ensuring everything was done right. But after reflecting on it, I realized that by not fully trusting my team, I was limiting their ability to grow and contributing to inefficiencies.\n
To address this, I began delegating more responsibility, trusting my team to handle challenges on their own, and stepping in only when necessary. Over time, this approach led to improved team morale, better decision-making, and allowed me to focus on higher-level strategic tasks. It was a tough lesson, but it made me a stronger and more effective leader.""")

    with st.expander("Tell me about a time you had to make a unpopular decision."):
        st.write("""When we launched the first version of our digital human product at CloudWalk, large language models were experiencing tremendous popularity. However, the initial version of our product didn’t have the model performance we wanted—it wasn’t delivering the level of quality and accuracy that our users would expect.\n
I made the unpopular decision to delay the launch of the product until we had improved the model’s performance. Instead of pushing out the unrefined version that was ready, I decided to hold off and use the additional time to fine-tune the model for better results. This wasn’t an easy choice, as the product team, sales, and other stakeholders were eager to release something in response to the high demand for large language models at that time.\n
I took the time to explain the situation to both the product manager and the sales team. I emphasized that releasing a suboptimal product could damage our brand’s reputation and lead to negative user experiences, which would ultimately hurt us more in the long run. I assured them that the additional time spent refining the model would pay off with better quality and user satisfaction.\n
At the same time, I worked closely with the machine learning team, prioritizing resources and closely managing the process to ensure we could improve the model quickly. We focused on fine-tuning and testing to achieve better performance.\n
Though this decision was unpopular, especially with the pressure to capitalize on the hype around large language models, it proved to be the right call. When we finally launched the improved version, the product was much better received by users, and it helped establish our product as a high-quality offering in the market.""")

    st.header("General questions")
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

    with st.expander("How do you make decisions when faced with incomplete or ambiguous information?"):
        st.write("""Decision-making in uncertain situations requires balancing speed and quality:\n
1. Gather Available Data:\n
  - I collect as much relevant data as possible within the given constraints. For example, during the early phases of developing the knowledge engine at CloudWalk, I relied on partial user feedback and historical project data to guide initial decisions.\n
2. Leverage Frameworks:\n
  - Decision Trees: I map out possible outcomes of each option, weighing their likelihood and impact.\n
  - Cost-Benefit Analysis: I compare the potential benefits of a decision against its risks and costs. For instance, when deciding whether to refactor the rendering engine for digital avatars, this approach helped me justify the resource investment.\n
3. Consult Experts:\n
  - I leverage the expertise within my team or network. Collaborative brainstorming often surfaces perspectives I hadn’t considered, reducing ambiguity.\n
4. Emphasize Iteration:\n
  - I adopt an iterative approach, making incremental decisions where possible. By starting small, such as building a proof-of-concept, I gather insights that guide the next steps.\n
5. Document Assumptions:\n
  - I ensure all decisions are accompanied by documented assumptions. If outcomes don’t align with expectations, this helps in revisiting and refining the decision.\n
This approach enables me to act decisively, even in ambiguous situations, while minimizing the risk of failure.""")

    with st.expander("What frameworks or principles guide your decision-making as a leader?"):
        st.write("""Several core principles guide my leadership decisions:\n
1. Data-Driven Approach:\n
  - Decisions should be backed by data whenever possible. For example, when deciding which features to prioritize for the digital avatar platform, I analyzed user behavior data and market research to ensure our efforts aligned with user needs and ROI.\n
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

    with st.expander("How do you work with people who might be technically excellent but hard to work with?"):
        st.write("""Working with someone who is technically excellent but difficult to collaborate with can be challenging, but it’s important to address the situation with professionalism *[prəˈfeʃənəlɪzəm]* and focus on achieving team goals.\n
- My approach begins with understanding the root cause of their behavior. I make an effort to build a rapport and find common ground by focusing on their strengths and the value they bring to the project. I also ensure that communication is clear and direct, setting expectations for collaboration and respecting their expertise while also asserting my own.\n
- For instance, in a previous project, I worked with a highly skilled engineer who was known for being challenging in team settings. I initiated one-on-one meetings to understand their perspective and address any concerns they had. During team meetings, I facilitated discussions to ensure everyone had the opportunity to contribute and be heard, while also keeping the focus on project objectives.\n
- I also worked on creating an environment where constructive feedback was encouraged, and I set up regular check-ins to monitor progress and address any issues promptly. By maintaining a focus on the shared goals and demonstrating respect for their technical expertise, we were able to work together more effectively.\n
- As a result, we successfully completed the project on time, and the engineer’s contributions were instrumental in its success. This experience taught me the importance of patience, clear communication, and finding ways to align individual strengths with team goals. It reinforced my belief that even challenging working relationships can lead to positive outcomes when managed with care and professionalism.""")

    with st.expander("Tell me about a time you solved a problem creatively."):
        st.write("""While working on the digital human product, we faced a challenge as users wanted to customize their own voices and avatars. Initially, with a small user base, the process was manual—users would send recordings via WeChat to our sales team, and our operations team would review the content to ensure quality. If the recordings didn’t meet the requirements, they had to be redone. Once approved, the recordings were passed to our machine learning engineers for custom model training. As the user base grew, this manual process became unscalable.\n
To address this, we developed a system that automated the entire process. Instead of relying on manual steps, we created a system where users could upload their audio and video recordings directly. The system provided step-by-step recording guides, and to make it engaging, we gamified the recording process—especially for audio, where there were more steps to follow. This made the experience less tedious for users.\n
On the backend, our operations team could review the uploaded content within the same system and provide feedback for improvements. Machine learning engineers were notified automatically when new training tasks were ready, and once the custom models were trained, they could be deployed with a single click. The system would then notify users that their personalized avatars were ready for use.\n
This automated solution not only scaled effectively with user growth but also enhanced the user experience and improved internal workflow efficiency.""")

    with st.expander("Since you've managed sub teams, are you still technically hands on?"):
        st.write("""Yes, I consider myself still technically hands-on. During my time at Google as a Tech Lead Manager, it was a core part of the role to stay hands-on, and I brought that mindset to my role at CloudWalk. As my team grew from about 20 to over 30 members, I had more time to contribute technically when the team was smaller. For example, when we started the digital human project, I stepped in to design the initial architecture since we hadn't yet found the right architect.\n
Additionally, given how rapidly AI and large language models are evolving, I prioritize staying informed about the technical details, especially the boundaries and capabilities of these technologies. This allows me to guide the team effectively and ensure we’re making the right decisions as we push the limits of AI. \n
Although my day-to-day responsibilities involve more management, I make a conscious effort to stay technically involved, particularly in the early stages of projects and during key architectural decisions.  I try my best to join most design reviews, discuss technical details in meetings with engineers, lead group studies on new advancements in LLM, and always proactively experiment with new technologies. This approach ensures that I stay connected to the technical aspects while empowering my team with the latest knowledge and tools.""")

    st.header("Managing individuals")
    with st.expander("Tell me about a few people on your team and the career development plans you created with them."):
        st.write("""In my current role at CloudWalk, I managed a diverse engineering team working on our digital human live-streaming product. I made it a priority to understand each team member’s career goals and worked closely with them to create tailored development plans.\n
One example is an architect with strong technical skills who wanted to take on leadership responsibilities. We created a development plan focused on expanding their leadership and management abilities, and I gave them the responsibility of leading the engineering development for our digital human product. I coached them in team management, communication, and resource allocation. Over time, they successfully transitioned into an engineering manager, driving key project milestones and leading a high-performing team.\n
Another example involves an engineer who was interested in moving into product management. I paired them with our product manager, where they had the opportunity to shadow and participate in planning meetings. Eventually, I gave them ownership of a feature, allowing them to manage both the technical and product aspects. This hands-on experience helped them transition into a hybrid product and engineering role.\n
In both cases, the development plans were designed to align their personal growth with the company's strategic needs. I also ensure that career development is an ongoing process, regularly checking in and adjusting plans to keep the team on track and motivated.""")

    with st.expander("What is the structure of your 1:1s? How do you run 1:1s with your team?"):
        st.write("""I hold weekly 1:1s with my direct report, and the structure is designed to balance project updates, feedback, and career development. I usually start by checking in personally to build rapport and understand how they’re doing outside of work. Then, we discuss their current projects, focusing on progress, challenges, and how I can help remove blockers. I make sure to provide feedback and ask for feedback in return, fostering an open communication environment.\n
We also regularly discuss career goals and growth opportunities. For instance, through regular 1:1 coaching, I’ve helped several teammates achieve promotions by working with them on priority management, communication strategies, and resource allocation. I adapt the structure based on each person’s needs, and I always follow up with action items to ensure accountability and continuous development.""")

    with st.expander("Have you ever promoted anyone? Describe the process."):    
        st.write("""I've helped several team members get promoted, but one case that stands out is when I first became a manager at Google.I promoted a junior engineer to a senior engineer role. This engineer had already shown strong technical skills and a proactive approach to problem-solving, but to move to the senior role, they needed to develop more leadership qualities and take ownership of larger projects.\n
The process began by assessing their performance against the expectations for senior engineers, which included not only technical proficiency but also leadership in mentoring, involvement in high-impact projects, and making architectural decisions. After identifying their potential, I worked with them to create a development plan focusing on enhancing their technical leadership, getting deeper into system design, and mentoring junior team members.\n
I then assigned them more challenging tasks, such as leading the design and execution of a major project. I also encouraged them to present their ideas during team meetings, which helped them build confidence in stakeholder communication and justifying technical decisions. We had regular 1:1s to track progress, and I ensured they gained visibility across the team and other groups.\n
Once they consistently demonstrated leadership and technical depth, I advocated for their promotion, highlighting their growth in influence and responsibility. After their promotion to senior engineer, they took on even more critical projects and became a mentor to others, significantly contributing to the team's success.\n
This experience not only boosted their career but also strengthened the team by adding a strong technical leader.""")

    with st.expander("How would you describe your role in coaching and career development?"):
        st.write("""As a coach, my role in career development is to help my team members grow both personally and professionally by providing guidance, feedback, and opportunities that align with their goals. I take an active interest in understanding their aspirations, strengths, and areas for improvement. Based on this, I work with them to create personalized development plans that focus on expanding their skills, building confidence, and preparing them for the next level in their careers.\n
I also make it a point to provide regular feedback during our 1:1s, ensuring that it's constructive and actionable. Whether it's technical skills or leadership abilities, I offer insights on how they can improve and continuously build on what they do well.\n
One of the key aspects of my coaching approach is giving team members the autonomy *[ɔːˈtɑːnəmi]* to take on new challenges. For example, I helped an architect on my team transition into an engineering manager role. We identified their potential for leadership, and I provided them with opportunities to lead cross-functional projects, manage resources, and build stronger relationships with other teams. I also coached them on team management, communication, and decision-making to ensure a smooth transition into the new role.\n
Overall, my role is to empower team members, foster an open and growth-oriented environment, and provide support when they need it, while holding them accountable for their progress. I believe that with the right guidance and opportunities, each individual can reach their full potential.""")

    with st.expander("Can you tell me about your leadership style?"):
        st.write("""My leadership style is flexible because I believe that different situations and team dynamics require different approaches. While I adapt my style based on the context, I primarily lean on a combination of visionary coaching and democratic leadership.\n
I’m a visionary leader in the sense that I set a clear vision for the team and inspire them by aligning their personal goals with the broader mission. I ensure that everyone understands the ‘big picture’ and how their work contributes to the overall success of the project. This helps the team stay motivated and focused, especially when tackling complex challenges or when there is a long-term goal to achieve.\n
At the same time, I employ a democratic style, encouraging open communication, collaboration, and input from team members in decision-making. I value diverse perspectives and actively seek feedback from the team to ensure everyone feels heard and empowered. This not only promotes a sense of ownership and accountability but also leads to better ideas and stronger team cohesion.\n
For example, at the beginning of a project, I set a clear vision for the product we were building and communicated how each team member’s work was integral to our success. I also made it a point to involve the team in key decisions, whether it was architecture design or project prioritization. By blending these styles, we were able to work together efficiently while also fostering a collaborative, empowered environment.""")

    with st.expander("Which leadership do you least prefer?"):
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
    with st.expander("Handle poor performers"):
        st.write("""When handling a poor performer, my first step is to assess the situation to understand the root cause. Sometimes, performance issues can stem from unclear expectations, personal challenges, or a lack of resources. I try to understand whether it's a skill gap, a motivation issue, or something else entirely.\n
Once I have a clear understanding, I have an open and honest conversation with the individual. I aim to provide specific, actionable feedback, focusing on what’s not working and why, while also acknowledging their strengths. It's important to approach this conversation with empathy, so they feel supported rather than attacked.\n
Next, I work with them to set clear goals and provide any resources or support they may need to improve, whether it’s additional training, mentorship, or adjusting their workload. I emphasize that improvement is expected, but I also make sure they understand the steps they can take to succeed.\n
I monitor progress regularly and provide feedback along the way. I follow up to see if the individual is on track and make adjustments if necessary. This also gives the person a chance to ask questions or raise concerns.\n
If the individual still doesn't show improvement despite my efforts, I take tough decisions if needed. This could mean reassignment, role adjustments, or, in extreme cases, separation from the team. Ultimately, my goal is to ensure the success of both the individual and the team, and sometimes that means making difficult decisions for the greater good.""")

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

    with st.expander("Layoff communication."):
        st.write("""This is a particularly challenging task, and I’ve only had one experience with it. At CloudWalk, due to a strategic shift, we decided to focus more on our Digital Human Platform and reduce resources on our B2B and Government client business. Unfortunately, this meant that we had to make some tough decisions, including laying off a Technical Project Manager who had a strong track record in B2B projects.\n
When I communicated the layoff, I made sure to be transparent and direct about the reasons behind the decision, explaining that it was based on the evolving company strategy and not related to the individual’s performance. I also made it clear that this was a difficult decision for the company, as their contributions had been highly valued.\n
I approached the conversation with empathy and respect. I acknowledged the impact this would have on the individual’s career and expressed gratitude for their hard work. During the conversation, I offered support, including severance[ˈsevərəns] packages, access to career coaching, and job placement assistance. I wanted to ensure they felt supported during this transition, and we discussed their next steps and options in detail.\n
Afterward, I communicated with the rest of the team, being honest about the changes while focusing on how we could all contribute to the company’s new direction. I wanted to keep morale high and reassure everyone that we were committed to providing support as we navigated through these changes together.""")

    with st.expander("How do you track and measure the success of your engineering team?"):
        st.write("""I use a combination of quantitative metrics and qualitative feedback to track and measure the success of my engineering team. Here’s how:  \n
1. **Delivery Metrics**: I measure the team’s ability to deliver on time and within scope. For example, during the development of the digital human product, we tracked sprint velocity, the number of features shipped, and the resolution of critical bugs to ensure we met project milestones.\n  
2. **Quality of Work**: Code quality and system reliability are key indicators. I track metrics such as test coverage, incident frequency, and user feedback. For instance, after optimizing the rendering engine pipeline, we saw a 5x improvement in efficiency, which validated the team’s technical success.\n  
3. **Team Productivity and Collaboration**: I assess productivity through task completion rates and cross-team collaboration effectiveness. Retrospective meetings help identify areas for improvement and foster continuous learning.\n  
4. **Impact on Business Goals**: I align the team’s performance with company or product outcomes. For example, the success of our digital human product—gaining over 10,000 paying users and generating millions in revenue—was a clear measure of the team’s impact.\n  
5. **Team Growth and Engagement**: I track individual development, promotions, and retention rates as indicators of a healthy team. I also gather feedback through one-on-ones to ensure team members feel supported and motivated.  \n
By combining these approaches, I ensure that my team is delivering value, growing professionally, and contributing to both short-term and long-term company goals.""")

    with st.expander("How do you ensure that your team is focusing on building scalable and sustainable solutions?"):
        st.write("""To ensure my team focuses on building scalable and sustainable solutions, I emphasize the following principles:  \n
1. **Start with Clear Requirements**: I ensure the team understands the long-term business needs and potential growth scenarios. For example, during the development of the digital human rendering platform, I emphasized scalability to support both small businesses and larger enterprises as the product gained traction.\n  
2. **Architect for Scalability Early**: I encourage designing systems with scalability in mind from the outset. For instance, we refactored our rendering engine system to handle real-time digital avatar rendering efficiently, optimizing the pipeline to accommodate more concurrent users without significant additional costs.\n  
3. **Leverage Best Practices**: I promote the use of proven frameworks, modular design, and cloud-native architectures to ensure systems are easy to extend and maintain. For example, in the RAG-based Q&A system, we used a microservices architecture to make individual components scalable independently.  \n
4. **Encourage Regular Refactoring**: I prioritize technical debt management by setting aside time for code reviews and refactoring. This ensures that short-term solutions don’t hinder long-term sustainability.  \n
5. **Monitor and Test Continuously**: I implement robust monitoring and load-testing practices to ensure systems perform well under expected and peak loads. For example, we stress-tested the digital avatar platform using simulated live-stream traffic to confirm it could handle spikes in demand.\n  
6. **Foster a Culture of Ownership**: I encourage the team to think beyond immediate goals, considering maintainability and scalability in every decision.  \n
These practices have consistently helped my teams deliver robust and future-proof solutions, balancing immediate deliverables with long-term sustainability.""")

    st.header("Managing team execution.")
    with st.expander("How would you motivate your team to perform better?"):
        st.write("""To motivate my team to perform better, I start by setting clear and achievable goals. When everyone knows what the objectives are and how their work contributes to the overall success of the team, it creates a sense of purpose and direction.\n
I also believe in giving my team ownership of their projects. When people feel that they have the freedom to make decisions and influence outcomes, their motivation naturally increases. I encourage autonomy but also make sure they know I’m there to support them if they need guidance.\n
Recognizing and celebrating both small wins and major accomplishments is key. I make sure to acknowledge team and individual contributions regularly, whether that’s through a quick shout-out in a meeting or a more formal recognition.\n
I’m also committed to my team’s personal and professional growth. I make sure to understand each team member’s career goals and provide opportunities for learning, whether that’s through training, stretch assignments, or mentorship. When people feel they’re growing, they’re more likely to stay engaged and motivated.\n
Finally, I lead by example. I show up with a positive attitude, a strong work ethic, and a commitment to the team’s goals. When my team sees that I’m fully invested, they tend to mirror that energy.\n
And of course, I always make an effort to address challenges they face. If there are blockers or difficulties, I work with them to remove obstacles[ˈɑːbstək(ə)lz], ensuring that everyone has the resources they need to succeed. This creates a supportive and motivated environment where the team can perform at their best.""")

    with st.expander("How do you manage multiple requests for your team, how do you deal with competing priorities?"):
        st.write("""As a manager, handling multiple requests and competing priorities is an essential part of my role. To manage this effectively, I use a combination of prioritization, clear communication, and resource allocation.\n
1. Prioritization: I start by assessing the urgency and impact of each request. I often use frameworks like Eisenhower Matrix or Impact vs. Effort analysis to help differentiate between what needs to be done immediately and what can be scheduled later. I focus on aligning requests with our strategic goals and company priorities, ensuring that tasks that will move the business forward are given the highest priority.\n
2. For instance, when we were working on the digital human product, there were often conflicting requests from both internal teams and external stakeholders. I had to prioritize features that aligned with the strategic focus on consumer-facing applications, while balancing the ongoing infrastructure needs. I communicated these priorities to the team clearly, so everyone understood what needed to be prioritized and why.\n
3. Clear Communication: I make sure that there’s constant, transparent communication with stakeholders about timelines, expectations, and trade-offs. When there’s a conflict between priorities, I bring key stakeholders together to discuss and agree on the best course of action. For example, when we had to choose between adding new features to the product or addressing technical debt, I had discussions with product managers, sales, and the tech team to come up with a solution that balanced both short-term deliverables and long-term stability.\n
4. Resource Allocation: Once priorities are set, I assess the current workload and availability of the team. If there are multiple high-priority tasks, I might reassign resources or shift timelines accordingly. I also make sure that the team is not overwhelmed by ensuring that they have a manageable workload and sufficient time to focus on high-impact work.\n
5. Delegation and Trust: I delegate tasks to the team based on their strengths and expertise, ensuring they have the autonomy to take ownership. For example, if I have multiple requests for different areas of the product, I might delegate certain tasks to team leads or senior engineers, empowering them to take responsibility and make decisions for their areas.\n
By balancing these approaches—prioritizing tasks based on business impact, maintaining open communication with stakeholders, managing resources effectively, and empowering the team—I can navigate competing priorities and ensure that the team delivers the best possible outcomes.""")

    with st.expander("how do you setup projects for success?"):
        st.write("""There are many factors that contribute to a successful project, but in my experience, three core elements stand out: clearly defining success, managing timelines effectively, and maintaining strong team communication and morale.\n
First, success starts with clarity. Before kicking off any project, I ensure we have a clear understanding of what success looks like. This often means delivering a project that solves a key business problem, meets the defined timelines, and keeps the team engaged and motivated. Achieving this requires early alignment across all key stakeholders, including engineers, product managers, and other departments like marketing and sales. This helps ensure that everyone understands the scope and purpose of the project before any development begins. I also take this opportunity to identify and plan for dependencies, ensuring that we’re not blocked by other teams or workstreams and looking for opportunities to parallelize tasks where possible.\n
When it comes to timelines, I collaborate closely with product and engineering to set realistic deadlines and break the project into well-defined milestones. I’ve found that it’s important to establish regular checkpoints and build in time for each phase, such as design, development, and QA. In many cases, I assign a senior engineer or DRI (Directly Responsible Individual) to own the technical leadership of the project. This person helps break down the project into actionable tasks and ensures that the team remains on track, adjusting as needed if we hit roadblocks.\n
Finally, I believe strong communication is crucial. Regular standups or syncs help keep the team aligned, especially when working with cross-functional or remote teams. These meetings uncover potential issues early, increase overall project velocity, and foster a culture of transparency. By proactively managing both progress and morale, the team is better equipped to overcome any challenges that arise.\n
While issues can sometimes put a project at risk, having this structure in place allows the team to navigate these challenges more effectively and keep the project moving toward success.""")

    with st.expander("How do you balance feature development and technical debt?"):
        st.write("""Technical debt is a natural part of development, especially when moving fast, but it’s important to manage it before it becomes a bottleneck. I usually dedicate around 20% of our development time to addressing technical debt, focusing on issues that impact performance, scalability, and team productivity. I work closely with the team to identify key areas of friction, and whenever possible, we try to address technical debt during feature development to avoid taking separate time away. However, when the debt is too large or impactful, we plan dedicated sprints to tackle it.\n
For instance, during the development of our digital human platform, we initially reused an existing resource scheduling framework to generate digital human videos. While it allowed us to move quickly at first, it soon became clear that the framework was inefficient and prone to frequent errors, which slowed down the entire process. The team spent a significant amount of time troubleshooting, which took away from feature development. Recognizing the long-term cost, we made the decision to refactor the entire system and build a dedicated resource scheduling system specifically optimized for digital human rendering. This effort paid off — We significantly improved rendering efficiency, drastically reduced errors, and created more time for future feature development. It was a clear example of how investing time in addressing technical debt can unlock greater velocity and stability for the team.""")

    with st.expander("How do you explain tech debt to non technical team members?"):
        st.write("""When explaining tech debt to non-technical team members, I usually compare it to financial debt. Just like borrowing money can help you achieve something quickly but comes with the need to repay it with interest, tech debt arises when we prioritize speed over perfect code or optimal solutions. It helps us move fast in the short term, but over time, we accumulate “interest” in the form of maintenance issues, bugs, or slower development.\n
Addressing tech debt requires time and resources, just like repaying financial debt, but if we don’t tackle it, it can slow down future progress and make new feature development harder or riskier.""")

    with st.expander("How do you measure your impact as an engineering manager?"):
        st.write("""Measuring my impact as an engineering manager involves evaluating contributions across three main areas: customer impact, organizational impact, and team impact. Here’s how I approach it:\n
1. Customer Impact: I assess how the work my team delivers affects our customers. This includes tracking the success of new features, monitoring customer satisfaction scores, and analyzing feedback. For example, when we release a new feature, I look at metrics like NPS scores and user engagement to gauge its effectiveness and ensure it meets customer needs.\n
2. Organizational Impact: I measure how well our work aligns with and supports the company’s strategic goals. This involves evaluating whether our projects contribute to revenue growth, enhance user base, or achieve other key performance indicators. I also consider how our work helps in meeting broader organizational objectives. For instance, if our team is tasked with a revenue-generating feature, I track its performance against revenue targets and how it influences overall business metrics.\n
3. Team Impact: I focus on the growth and development of my team members. This includes tracking their career progression, satisfaction, and overall productivity. I regularly conduct one-on-ones to understand their goals and how well our projects align with their career aspirations. Additionally, I measure the efficiency improvements from addressing technical debt and optimizing processes. For example, if we streamline our build process and reduce build times, I assess how this improvement affects team productivity and morale.\n
To ensure I’m effectively measuring impact, I use a combination of quantitative metrics and qualitative feedback. I also make sure to set clear milestones and KPIs for projects and regularly review progress against these indicators. By maintaining this balance, I can better understand and communicate the value my team and I are delivering.""")

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
Gather Inputs: I start by aligning with senior leadership to understand company goals, gather feedback from internal customers through surveys, and collect insights from my team on technical challenges and opportunities.\n
Plan and Prioritize: Using this data, I create and prioritize a list of goals based on impact and feasibility, considering KPIs like scalability, security, and balancing innovation with tech debt.\n
Define and Communicate Goals: I set clear, actionable goals, often using OKRs or roadmaps, and include stretch goals to motivate the team with ambitious targets.\n
Execution and Review: I ensure capacity planning aligns with goals and monitor progress through regular check-ins. If issues arise, we conduct blameless retrospectives to learn and improve.\n
Motivation and Support: I maintain transparent communication about goal prioritization and align tasks with team members' interests and career growth opportunities, framing even challenging tasks as learning experiences.\n
This approach ensures well-rounded, achievable goals that drive both team and personal development.""")

    st.header("Cross functional collaboration")
    with st.expander("How do you balance engineering limitations with customer requirements?"):
        st.write("""Balancing engineering limitations with customer requirements is a constant challenge, but it’s key to ensuring both technical feasibility and customer satisfaction. My approach typically involves a combination of listening, technical assessment, and prioritization.\n
First, I always start by deeply understanding the customer requirement. I aim to clarify not only what the customer is asking for but also why it’s important for them. Understanding the underlying business goals helps me think creatively about potential solutions. Sometimes, there might be alternative ways to meet the same objectives with less complexity or cost. For example, when we began developing our digital human product, we faced significant complaints about the slow rendering speeds. After gathering user feedback, I researched the situation thoroughly and discovered two key points: 1) rendering was indeed slow, with a 1-minute video taking over 10 minutes to render, and 2) users were frustrated because they had no idea how long the rendering would take or when it was complete.\n
After understanding the requirements, I evaluated the technical feasibility and communicated transparently with both the customer and internal stakeholders. During this communication, I found that users understood rendering takes time and were willing to wait; what they disliked was the uncertainty about how long they would have to wait. I identified the need for optimizing server utilization and improving the efficiency of the rendering pipeline. Additionally, I realized that we could speed up the process significantly by splitting a one-minute video into smaller segments that could be rendered in parallel across multiple servers. To improve the user experience, I proposed providing accurate estimates of rendering times, implementing a progress bar so users could see how much of the video had been rendered, and creating a notification system to alert them as soon as their rendering tasks were completed. This way, users no longer had to wonder how long it would take or keep checking back for the final result.\n
Finally, I aligned the customer requests with the broader engineering roadmap, assessing how they fit with our current priorities and business goals. Once that was established, I communicated with both the users and stakeholders to outline a timeline for the improvements, assuring them that we would deliver an initial version quickly to enhance the user experience while committing to ongoing optimizations. For high-impact but resource-intensive requests, I collaborated with the team to negotiate realistic timelines and identify a balanced approach. By employing a phased strategy, we were able to ensure timely progress on the project without overwhelming the engineering team.\n
Ultimately, it’s about maintaining open communication, understanding the real problem, and finding creative solutions that meet both technical constraints and customer needs. This approach has allowed me to maintain a balance between engineering efficiency and delivering value to customers.""")

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

    st.header("Technical Focus")
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
  - Our primary goals were high-quality voice output, real-time performance, and compatibility with our digital avatar system.\n
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

    with st.expander("How do you encourage innovation while ensuring alignment with technical constraints?"):
        st.write("""Encouraging innovation while respecting constraints requires fostering creativity within a structured framework:\n
1. Promote Exploration:\n
  - I allocate dedicated time for research and experimentation, such as hackathons or innovation sprints. For example, during the digital human project, team members explored using GANs for realistic avatar facial animations, which eventually became a differentiating feature.\n
2. Set Clear Guardrails:\n
  - I define non-negotiable constraints like performance, scalability, or compliance. Within these boundaries, the team has freedom to experiment. For instance, when optimizing rendering, we constrained GPU usage to consumer-grade devices, which inspired innovative pipeline improvements.\n
3. Encourage Knowledge Sharing:\n
  - I create an environment where ideas are shared freely through tech talks, code reviews, and brainstorming sessions. Collaboration often sparks new approaches while identifying practical challenges early.\n
4. Celebrate Wins and Learn from Failures:\n
  - Recognizing and rewarding innovative contributions motivates the team to think creatively. Equally, I encourage learning from failures, ensuring a no-blame culture that values experimentation.\n
5. Iterative Approach:\n
  - I advocate for building prototypes to validate ideas quickly. For example, we built a lightweight version of the live Q&A system using RAG models before scaling it to production.\n
6. Cross-functional Collaboration:\n
  - By involving stakeholders early, such as product managers and designers, I ensure innovative ideas align with business needs and constraints.\n
Through this balanced approach, I enable my team to innovate while ensuring technical feasibility and alignment with organizational goals.""")

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

    with st.expander("How do you balance hiring externally versus promoting or developing internal talent?"):
        st.write("""I believe in promoting internal talent whenever possible because it boosts morale, retains institutional knowledge, and shows team members that their growth is valued. I regularly assess team members' readiness for new challenges and provide growth opportunities through stretch assignments and mentorship. \n
However, hiring externally has the benefit of bringing fresh perspectives and new expertise, which can be particularly valuable in addressing skill gaps or driving innovation. If there is a rapid growth in the team’s scope or responsibilities, I also prioritize external hires to quickly scale the team and ensure we can meet the demands of the expanded scope.""")

    with st.expander("How do you assess soft skills during the interview process?"):
        st.write("""I design behavioral interview questions to evaluate communication, collaboration, and problem-solving skills. For example, I ask candidates to describe a time they handled a conflict in a team or how they influenced others without direct authority.\n 
To ensure a well-rounded assessment, I involve multiple interviewers and ask them to evaluate soft skills from different perspectives, such as teamwork, adaptability, and empathy. \n
Additionally, the way candidates communicate during technical problem-solving exercises serves as an implicit assessment of their soft skills. I observe how they explain their thought process, seek clarification, and respond to feedback, as these interactions provide valuable insights into their communication and collaboration abilities.""")

    with st.expander("Have you ever had a bad hire, and how did you address the situation?"):
        st.write("""When I started working at CloudWalk, I hired an engineer who was technically strong but struggled to collaborate effectively. They frequently had conflicts with teammates, which negatively impacted team dynamics. I tried to address the issue by providing clear and direct feedback, focusing on specific instances where their behavior caused friction, and worked with them on strategies to improve their communication and collaboration skills.\n 
Despite ongoing coaching and support, the situation didn’t improve, so I worked with HR to transition them out of the role. This experience reinforced the importance of assessing both technical skills and cultural fit during the interview process and led me to refine our process by incorporating structured behavioral questions and involving multiple interviewers to evaluate interpersonal skills more thoroughly.""")

    with st.expander("What is your strategy for onboarding new hires effectively?"):
        st.write("""I start by creating a tailored onboarding plan that includes clear goals for the first 30, 60, and 90 days. I assign a mentor or buddy to help the new hire acclimate to the team and ensure they have access to necessary resources. I also schedule regular check-ins to provide feedback, answer questions, and address challenges. This approach helps new hires feel supported and productive quickly.\n
When I first joined Google, I started a 'Noogler' documentation to document my learning journey and onboarding experience. This document became a valuable resource for every new hire after me and was continuously enhanced by each new Noogler. At CloudWalk, I introduced the same practice, asking new hires to document their onboarding experience and update the guide to ensure it stays relevant and useful. This not only helps new hires feel supported and productive quickly, but also creates a culture of continuous improvement and shared knowledge.""")

    with st.expander("How do you handle high-volume hiring while maintaining quality?"):
        st.write("""As an engineer, my experience taught me only distributed systems can handle high-volume problems. I prioritize scalability by implementing a distributed and streaming approach to handle high-volume hiring effectively. \n
For example, I standardize interview questions and rubrics to ensure consistency, use automation tools to filter resumes, and integrate online assessment tools for an initial evaluation of candidates' technical and problem-solving skills.\n 
I also set up an interviewer pool by training a group of team members to conduct interviews, enabling us to scale the process while maintaining quality. \n
Additionally, I work closely with recruiters to align on the most critical skills and competencies, ensuring that every stage of the process remains focused and efficient.""")

    with st.expander("How do you ensure diversity and inclusion in your hiring process?"):
        st.write("""I focus on sourcing candidates from diverse backgrounds by partnering with organizations and communities that prioritize underrepresented groups in tech. \n
During the interview process, I implement structured interviews and standardized rubrics to reduce bias. I also train interviewers on unconscious bias and ensure diverse representation on the interview panel.\n 
Finally, I evaluate the process to identify potential barriers for candidates and continuously improve.""")

    with st.expander("How do you manage expectations between recruiters and hiring managers?"):
        st.write("""I start by clearly defining the role requirements and agreeing on a timeline with recruiters. I maintain regular communication through weekly syncs to review the pipeline, provide feedback, and adjust strategies as needed. I also set realistic expectations about the talent market and emphasize a focus on quality over speed to ensure long-term success.""")

with tab3:
    with st.expander("Tell me about a project you are proud of."):
        st.write("""I’m particularly proud of a project I led at CloudWalk, where we developed a digital human live-streaming product. CloudWalk is an AI company that traditionally focused on B2B and government clients, but we saw an opportunity to leverage the growing interest in large language models, especially after the rise of ChatGPT, to explore consumer-facing applications.\n
The idea came about while we were working on a knowledge engine product for enterprise clients. We had a few e-commerce clients in the live-streaming industry who needed intelligent customer service solutions. This sparked an idea: in China, live-streaming e-commerce is huge, but it's also very expensive to hire human hosts, and the barriers to entry are high. We thought, why not build a solution where digital humans could assist or even partially replace live hosts?\n
We created a product that allows users to select a virtual host’s appearance and voice, generate product scripts automatically, and even set up interactive features to engage with viewers. This product became incredibly successful and was adopted as a core strategic application within the company, generating millions of RMB in revenue. It’s one of the projects I’m most proud of because it not only solved a real problem in the market but also demonstrated the power of AI-driven innovation.""")

    with st.expander("Why did you decide to initiate the project?"):
        st.write("""I decided to initiate the digital human product because I saw a clear opportunity in the live-streaming e-commerce space. Through my research, I noticed several pain points in the industry, especially in China—live hosts are expensive, and it’s tough for smaller businesses to break in. With the rise of large language models (LLMs) and advancements in AI, it became clear that we could automate much of the live-streaming process, from creating personalized virtual hosts to generating scripts and interactive features.\n
I also saw that this digital human product fit perfectly with the growing demand for scalable, AI-powered solutions. By combining the intelligence of large language models with digital avatars—where AI acts as the "brain" and the avatars as the "body"—we could reduce costs while engaging audiences in ways traditional methods just can't match. This approach allows businesses to connect with their customers in a more dynamic and cost-effective way, while solving real-world challenges.\n
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

    with st.expander("What do you want to do to enhance the product?"):
        st.write("""There are three key areas I’d like to focus on for enhancing the digital human product:\n
Improving Visual Quality: Currently, our solution based on Wav2Lip is approaching its limits. While it works well for simple lip-syncing, it doesn’t capture more complex expressions or gestures. Diffusion-based methods, which are emerging in research, offer a way to generate not only matching lip movements but also facial expressions and even body movements, taking the realism to a whole new level. Although these methods aren't yet widely adopted in industry due to cost and rendering speed, I believe continuing to explore and optimize them will lead to a major leap in quality.\n
Enhancing Script and Response Generation: Another area I’d focus on is improving the quality of live-stream scripts and automatic responses generated by our large language models. While the current scripts are functional, they can feel somewhat robotic. I want to refine the model to generate more personalized, stylized text that aligns with the brand or persona of the digital human. For automatic responses, there’s still room to improve—sometimes the replies are off-target or too mechanical. By enhancing both the base model and retrieval-augmented generation, we can make interactions feel more natural and engaging.\n
Building a User Community Platform: As more users adopt the digital human product, I’d like to create a platform where users can share their creations, like videos or live streams. This would allow users to see each other’s work, foster creativity, and increase engagement. A community-driven platform could also serve as a way for users to learn from each other and grow their capabilities, leading to a more active and loyal user base.""")

    with st.expander("What are some of the enhancement technically."):
        st.write("""产品维度：出海，技术维度：算法维度：""")

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
        st.write("""To enhance script generation, we implemented a three-step process:\n
Data Collection and Processing: We crawled a large volume of live-stream data and used ASR (Automatic Speech Recognition) to convert the audio into text. We then utilized Large Language Model to clean, deduplicate, and filter this data to ensure its quality. The processed text became part of our base dataset, capturing real-world live-stream scenarios.\n
Continued Pre-Training: After preparing the data, we used it to continue pre-training our foundational large language model. By exposing the model to live-stream-specific data, we improved its ability to understand and generate live-stream scripts tailored to this unique style, where engaging and persuasive communication is essential.\n
Fine-Tuning with Human-Annotated Data: We handpicked high-quality live-stream sessions for manual annotation and used this annotated data to fine-tune the model. This step ensured that the model could generate scripts that met specific requirements for live-streaming. We extended this fine-tuning process to other tasks, including generating interactive scripts and short video scripts, to broaden the model's application across various content needs.""")

    with st.expander("Explain what did you do to enhance RAG to better support live interaction."):
        st.write("""To enhance Retrieval Augmented Generation (RAG) for better live interaction, we focused on four key improvements:\n
1. **Multi-Channel Retrieval**: We implemented a multi-channel retrieval strategy, combining **vector-based retrieval** using the **M3E-large model** with traditional **BM25 retrieval**. This allowed us to leverage both semantic and keyword-based retrieval methods, ensuring a more comprehensive set of results. The vector-based approach captured the deeper meanings behind user queries, while BM25 ensured precise matches for specific terms.\n
2. **Re-Ranking with BGE-Reranker**: After retrieving the candidate responses, we used the **BGE-reranker** to re-order the results based on their semantic relevance to the query. This re-ranking step ensured that the most contextually appropriate and useful responses were prioritized for the live interaction, improving the overall user experience.\n
3. **Document Processing with Large Language Models:** We utilized large language models to summarize and organize user-uploaded documents, transforming unstructured content into concise, relevant material for easier retrieval. First, we pre-processed answers to common queries like return policies and discount rules, making these responses readily available for live interactions. Next, we curated a category-specific FAQ list based on frequently asked questions from previous live-streams. When a user uploads a product, the system automatically identifies its category and suggests relevant FAQs. Additionally, we structured user documents into **knowledge graphs**, organizing product information into entities and using models to extract relevant attributes for more accurate content retrieval.\n
4. **User Interaction Input Understanding:** We first used a fine-tuned model to identify which audience inputs required a response, then classified them by intent, such as product features or discount information. Short and simple audience queries often lacked enough context for accurate retrieval. To address this, we fine-tuned the LLM to rewrite and expand these queries before retrieving relevant information. We also experimented with generating an initial response using the LLM (even if not fully accurate) and then combined it with the original query to improve retrieval effectiveness. This approach significantly enhanced **retrieval accuracy and diversity**, making the responses more relevant. \n
Overall, these enhancements led to a more engaging and effective live-stream interaction experience, ensuring users received timely and accurate information.""")

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
        st.write("""""")

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
