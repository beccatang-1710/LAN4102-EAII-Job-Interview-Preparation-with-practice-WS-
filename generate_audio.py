import asyncio, os, edge_tts

DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "audio")
VOICE = "en-GB-LibbyNeural"  # UK female, casual, energetic

TEXTS = {}

# ── speechTexts: intro (Tab 1) ──
TEXTS["intro_0"] = "Good morning. Thank you for having me here today."
TEXTS["intro_1"] = "My name is Sharon, and I'm a Higher Diploma student in Landscape Architecture at HKDI."
TEXTS["intro_2"] = "I'm excited to be here, to discuss my passion for sustainable design, and how I can contribute to your team."
TEXTS["intro_3"] = "During my Higher Diploma studies, I excelled in courses that covered site analysis and urban planning, which equipped me with essential knowledge to tackle real-world challenges."
TEXTS["intro_4"] = "I believe my academic background has prepared me well for this role."
TEXTS["intro_5"] = "I worked at ABC Design Firm last summer as an intern, where I had the opportunity to assist in landscape mapping."
TEXTS["intro_work2"] = "This experience allowed me to apply my knowledge in a practical setting, and enhanced my skills in communication, collaboration, and problem-solving."
TEXTS["intro_6"] = "In my leisure time, I enjoy sketching nature, which helps me stay inspired and informed about the latest trends."
TEXTS["intro_7"] = "Thank you for considering my application."
TEXTS["intro_8"] = "I look forward to the possibility of working together and contributing to your team."

# ── speechTexts: advanced (Tab 2) ──
TEXTS["adv_greeting"] = "Good morning. Thank you for having me here today. My name is Ava, and I'm a final-year student at the Hong Kong Design Institute studying for a Higher Diploma in Fashion Design. I'm excited to be here to discuss my passion for fashion."
TEXTS["adv_setting"] = "My love of fashion started in secondary school. I admired the experimental styles of brands like Balenciaga, Adidas Y-3, and Supreme."
TEXTS["adv_struggle"] = "but I couldn't afford them. I thought the fashion world was exclusive and not meant for a student from an ordinary background."
TEXTS["adv_realisation"] = "However, after learning about the humble beginnings of famous designers like Vivienne Westwood and Giorgio Armani, I realised how designers can come from diverse backgrounds and have a major impact in the world of fashion."
TEXTS["adv_solution"] = "This inspired me to become a fashion designer who creates original and multifunctional outfits that are affordable for everyone."
TEXTS["adv_education"] = "To pursue this dream, I began studying Fashion Design and have built a solid knowledge of fashion illustration, textile design, and garment manufacturing. For my graduation project, I created a fashion lookbook for a new streetwear brand to display its autumn collection. This experience enhanced my prototyping skills and taught me the importance of incorporating user feedback into my designs."
TEXTS["adv_experience"] = "Additionally, I completed my industrial attachment at a fashion retailer, where I assisted designers in sketching and creating 3D models of knitwear. These hands-on experiences allowed me to apply my knowledge in a real-world setting."
TEXTS["adv_hobbies"] = "In my spare time, I enjoy reading fashion magazines to stay inspired and informed about the latest trends. I believe that maintaining a fresh perspective is essential in the fast-paced fashion industry."
TEXTS["adv_closing"] = "Overall, I consider myself a dedicated and creative person eager to make a positive impact in your company, and I look forward to bringing my skills and enthusiasm to your team."

# ── speechTexts: questions (q_0 to q_26) ──
TEXTS["q_0"] = "What are your goals for the next five or ten years? How do you plan to achieve those goals?"
TEXTS["q_1"] = "What are your long-term career goals?"
TEXTS["q_2"] = "What is your personal growth and development plan?"
TEXTS["q_3"] = "Would you consider taking any training courses related to this field or job?"
TEXTS["q_4"] = "What would you like to study in the near future?"
TEXTS["q_5"] = "What are your strengths or weaknesses?"
TEXTS["q_6"] = "What three words would you use to describe yourself?"
TEXTS["q_7"] = "What do you do in your spare time?"
TEXTS["q_8"] = "How are your studies at IVE related to this job?"
TEXTS["q_9"] = "What have you learnt at IVE to prepare you for this job?"
TEXTS["q_10"] = "What is your favourite subject at IVE? What have you learnt from it?"
TEXTS["q_11"] = "What skills or knowledge have you acquired from your full-time or part-time work?"
TEXTS["q_12"] = "What have you gained from your summer work, part-time work, or voluntary work?"
TEXTS["q_13"] = "Describe a difficult work situation or project, and explain how you overcame it."
TEXTS["q_14"] = "How would you deal with difficult customers, patients, or colleagues?"
TEXTS["q_15"] = "How would you manage multiple tasks?"
TEXTS["q_16"] = "Can you tell us about a situation in which you were required to solve a complicated problem?"
TEXTS["q_17"] = "Describe a time when you worked well under pressure. How did you handle the situation?"
TEXTS["q_18"] = "Can you provide us with an example of your ability to work independently?"
TEXTS["q_19"] = "Do you work better as a team member or alone? Give an example."
TEXTS["q_20"] = "What do you know about our company?"
TEXTS["q_21"] = "What interests you about this job?"
TEXTS["q_22"] = "Why do you want this job?"
TEXTS["q_23"] = "Since you are quite fresh compared to other candidates, what makes you think you are qualified for the post?"
TEXTS["q_24"] = "What makes you think you are a suitable candidate for the post?"
TEXTS["q_25"] = "What can you contribute to our company?"
TEXTS["q_26"] = "Why should we hire you?"

# ── Worksheet questions (Tab 3-7 inline speak calls) ──
TEXTS["ws_c1_q1"] = "Question 1. Can you please introduce yourself in 2 minutes?"
TEXTS["ws_c1_q2"] = "Question 2. What do you do in your spare time?"
TEXTS["ws_c1_q3"] = "Question 3. I see you have done some voluntary work. What did you learn from that?"
TEXTS["ws_c1_q4"] = "Question 4. What three keywords would your peers use to describe you?"
TEXTS["ws_c2_q1"] = "Question 1. Can you describe a time when your strengths helped you succeed?"
TEXTS["ws_c2_q2"] = "Question 2. What is a weakness you've identified in yourself, and how are you addressing it?"
TEXTS["ws_c2_q3"] = "Question 3. What are the important qualities a person should have to become an effective team member?"
TEXTS["ws_c2_q4"] = "Question 4. How do you ensure your weaknesses do not impact your work performance?"
TEXTS["ws_c2_q5"] = "Question 5. In what areas do you feel you need the most improvement?"
TEXTS["ws_c3_q1"] = "Question 1. What is your plan for your personal growth and development?"
TEXTS["ws_c3_q2"] = "Question 2. What are your long-term career goals?"
TEXTS["ws_c3_q3"] = "Question 3. What are your goals for the next 5 or 10 years?"
TEXTS["ws_c3_q4"] = "Question 4. What would you like to study in the near future?"
TEXTS["ws_c3_q5"] = "Question 5. Will you consider taking any training courses related to this field or job?"
TEXTS["ws_c4_q1"] = "Question 1. How do you deal with difficult customers or irresponsible colleagues?"
TEXTS["ws_c4_q2"] = "Question 2. How do you manage multiple tasks?"
TEXTS["ws_c4_q3"] = "Question 3. How do you handle office gossip?"
TEXTS["ws_c4_q4"] = "Question 4. Describe a difficult work situation or project and how you overcame it."
TEXTS["ws_c4_q5"] = "Question 5. Can you tell us about a situation where you analysed and solved a complicated problem?"
TEXTS["ws_c4_q6"] = "Question 6. How do you deal with conflicts with peers?"
TEXTS["ws_c5_q1"] = "Question 1. Do you work better as a team member or alone? Why?"
TEXTS["ws_c5_q2"] = "Question 2. Can you provide an example of your ability to work independently?"
TEXTS["ws_c5_q3"] = "Question 3. How do you handle stress and pressure?"
TEXTS["ws_c5_q4"] = "Question 4. Do you mind traveling frequently to Mainland China?"
TEXTS["ws_c5_q5"] = "Question 5. Are you willing to work under pressure and overtime?"
TEXTS["ws_c5_q6"] = "Question 6. Do you have any full-time or part-time work experience?"
TEXTS["ws_c5_q7"] = "Question 7. What have you gained from your summer work or part-time work?"
TEXTS["ws_c5_q8"] = "Question 8. What do you know about the type of work we expect from you?"

# ── Example texts (from .ws-example divs) ──
TEXTS["ex_c1_q1"] = "Hi, my name is Sharon, you can call me Sherry. I graduated from IVE with a Higher Diploma in Landscape Architecture this summer. I have worked at ABC Design Firm as a part-time intern, where I had to assist with landscape mapping and site visits. I have gained better communication and time management skills. I am hardworking and responsible. I am confident that I will be a suitable person for this job."
TEXTS["ex_c1_q2"] = "In my spare time, I like to paint and draw to relax. I often explore new painting methods that could enhance my skills."
TEXTS["ex_c1_q3"] = "At my volunteering, I learnt to work with others, communicate with my team members, and manage time when doing projects."
TEXTS["ex_c1_q4"] = "They would say I am hard-working and responsible, because I often work overtime to complete all my tasks. They would say I have a good sense of responsibility, because I often work overtime to complete all my tasks."
TEXTS["ex_c2_q1"] = "There's a time when my attention to detail helped me succeed in a project. I was responsible for checking the report before it was submitted. I noticed some small errors that could have caused problems. By fixing those mistakes, the result was the report was much clearer, and we received positive feedback."
TEXTS["ex_c2_q2"] = "Sometimes I might find it challenging to meet tight deadlines. I'm working on improving my time management. I have started using project management apps and making daily to-do lists. This has helped me manage my schedule better."
TEXTS["ex_c2_q3"] = "To be an effective team member, a person should have good communication skills. This helps everyone understand each other. They should also be reliable, so others can depend on them to complete tasks. Finally, being open to feedback is important, as it helps improve the team's performance."
TEXTS["ex_c2_q4"] = "I regularly review my tasks to identify any weaknesses. For example, if I struggle with public speaking, I practice my presentations in front of friends. I also ask for feedback to improve. By being aware and taking action, I make sure my weaknesses do not affect my performance."
TEXTS["ex_c2_q5"] = "I feel I need the most improvement in my networking skills. Sometimes I find it hard to connect with new people. To work on this, I am attending networking events and practicing my conversation skills. This way, I hope to build better relationships in my professional life."
TEXTS["ex_c3_q1"] = "My plan includes setting clear goals for my skills and knowledge. I aim to take online courses related to my field, seek feedback from colleagues, and attend relevant workshops. I believe continuous learning will help me grow personally and professionally."
TEXTS["ex_c3_q2"] = "My long-term goal would be advancing in my career to take on leadership roles, also continuously improving my skills, as well as make a positive impact in my field and help others grow along the way."
TEXTS["ex_c3_q3"] = "In the next five years, I aim to deepen my expertise in my field and take on more responsibilities, possibly in a leadership position. In ten years, I hope to be in a senior role where I can influence strategy and mentor others. To achieve these goals, I plan to pursue relevant certifications, seek mentorship, and focus on building a strong professional network."
TEXTS["ex_c3_q4"] = "In the near future, I would like to study video-editing. I believe this knowledge will enhance my abilities and help me contribute more effectively to my team and the company."
TEXTS["ex_c3_q5"] = "Positive. I am definitely open to taking relevant training. I believe that ongoing education is important for keeping up with industry trends and upgrading my skills."
TEXTS["ex_c4_q1"] = "When dealing with difficult customers, I stay calm and listen to their concerns. I would try to understand their point of view and find a solution together. For irresponsible colleagues, I communicate openly with them about the issues. I suggest ways to improve our teamwork, focusing on positive outcomes."
TEXTS["ex_c4_q2"] = "To manage multiple tasks, I prioritise them based on deadlines and importance. I use a planner to write down what needs to be done daily. This helps me stay organised and focused. I also set small goals for each task, which makes it easier to complete them."
TEXTS["ex_c4_q3"] = "When I hear office gossip, I try to avoid participating in it. Instead, I focus on my work and encourage others to do the same. If the gossip affects my team, I may talk to a manager to address the issue professionally."
TEXTS["ex_c4_q4"] = "In a previous project, we faced a tight deadline with limited resources. I organised a meeting to discuss the challenges with my team. We divided the work into smaller tasks and supported each other. By staying focused and working together, we completed the project on time and met our goals."
TEXTS["ex_c4_q5"] = "Once, I had to analyse a drop in sales for our product. I collected data and identified that customers were confused about its features. Then I proposed a new marketing strategy with clearer information. After implementing it, sales improved significantly, showing the importance of good analysis."
TEXTS["ex_c4_q6"] = "When I have a conflict with a peer, I would first try to understand their perspective. I then approach them calmly and discuss the issue openly. If needed, I would involve a manager to help us resolve the conflict professionally."
TEXTS["ex_c5_q1"] = "I prefer to work as a team member because I like to hear other people's opinions. But I don't mind working alone. Or I prefer to work alone so I can focus better on details. But I don't mind working in a team as well."
TEXTS["ex_c5_q2"] = "When I was studying, I had to work on individual projects and come up with a business plan or design concept or an app design, where I spent hours researching and working on it. At the end, I was able to finish before the deadline."
TEXTS["ex_c5_q3"] = "I like to play basketball, as it helps me relax."
TEXTS["ex_c5_q4"] = "No, I don't mind at all. I am happy to be able to see how things work in China as well."
TEXTS["ex_c5_q5"] = "Yes, I don't mind working overtime to get things done."
TEXTS["ex_c5_q6"] = "Yes, I have been working at a convenience store as a part-time salesperson, where I was responsible for the cash register and the overall organisation of the store."
TEXTS["ex_c5_q7"] = "I am able to communicate better and work better with others and manage time better when I worked as a salesperson."
TEXTS["ex_c5_q8"] = "Since it is an entry level position, I would expect to be helping colleagues with anything they need assistance with."

async def main():
    os.makedirs(DIR, exist_ok=True)
    for key, text in sorted(TEXTS.items()):
        path = os.path.join(DIR, key + ".mp3")
        if os.path.exists(path):
            print(f"SKIP  {key}.mp3")
            continue
        print(f"GEN   {key}.mp3 ...", end=" ", flush=True)
        communicate = edge_tts.Communicate(text, VOICE)
        await communicate.save(path)
        size = os.path.getsize(path)
        print(f"DONE ({size} bytes)")

asyncio.run(main())
print(f"\nAll done. {len(TEXTS)} files. Saved to:", DIR)
