from flask import Flask, request, jsonify, Response, render_template
from flask_cors import CORS

app = Flask(__name__)


api_v1_cors_config={
       "origin" : ["http://localhost:5000"],
       "methods" : ["GET"]
}

CORS(app, resources={
       r"/fortuneTelling" : api_v1_cors_config
})

@app.route('/fortuneTelling', methods=['GET'])
def fortuneTelling():
      if request.method == 'GET':
            name = request.args.get('name')
            age = request.args.get('age')
            gender = request.args.get('gender')
            question = request.args.get('question')

            answer= ""
            if question == "1":
                        if age < "30":
                              if 'J' in name:
                                    answer = ("I sense a strong and dynamic energy surrounding your career path, especially given your age"
                                          ". The next few years will be pivotal for you. There are opportunities coming"
                                          "your way that will require you to step out of your comfort zone, but they will lead to significant" 
                                          "growth and advancement. I see a change or a major decision on the horizon, perhaps within the next "
                                          "6 to "
                                          "12 months. This could be a promotion, a new job offer, or even a shift in your career focus. Trust "
                                          "your "
                                          "instincts during this time and be open to new possibilities. Your ability to adapt and your natural "
                                          "charisma will play a crucial role in your success. Networking and building strong professional "
                                          "relationships will open doors for you. Keep honing your skills and don't be afraid to pursue further"
                                          "education or training if an opportunity arises. Financially, you will see gradual improvement, "
                                          "especially if you are mindful of saving and investing wisely. Remember, persistence and dedication "
                                          "are "
                                          "key. Your hard work will pay off, and you will find yourself in a position of greater stability and "
                                          "satisfaction. Overall, your career fortune looks promising, with growth, learning, and new "
                                          "opportunities"
                                          "paving the way to a bright future. Stay confident, keep pushing forward, and embrace the changes "
                                          "that "
                                          "come your way.")
                              elif 'K' in name:
                                    answer = ("I sense a vibrant and determined energy surrounding your career path. Your career fortune holds "
                                          "exciting"
                                          "and transformative opportunities ahead. The coming years will be instrumental in shaping your "
                                          "professional journey. You are on the cusp of a significant breakthrough. Within the next year, "
                                          "there is "
                                          "a high likelihood of encountering a pivotal opportunity. This could manifest as a promotion, "
                                          "a new job "
                                          "offer, or even an entrepreneurial venture. Trust in your abilities and be ready to seize the moment "
                                          "when it arrives."
                                          "Your natural leadership skills and innovative thinking will be key assets. I see you taking on roles"
                                          "that challenge you and push you to grow, but your resilience and creativity will help you overcome "
                                          "any obstacles. Networking and building strong connections will also play a crucial role in your "
                                          "success."
                                          "Financially, I foresee a steady improvement, especially if you focus on making smart investments and"
                                          "saving wisely. It's important to be strategic with your finances to ensure long-term stability and "
                                          "growth."
                                          "Overall, your career fortune is filled with potential and promise. Embrace the changes, stay "
                                          "confident "
                                          "in your path, and continue to push your boundaries. The hard work you invest now will lead to a "
                                          "fulfilling and prosperous career.")
                              elif "T" in name:
                                    answer = ("I sense a strong and ambitious energy surrounding your career path. "
                                          "Your career fortune holds promising and exciting opportunities that will unfold over the next few "
                                          "years."
                                          "You are entering a period of growth and transformation. Within the next 6 to 18 months, you will "
                                          "likely "
                                          "face significant opportunities that could change the trajectory of your career. This might come in "
                                          "the "
                                          "form of a promotion, a new job offer, or even a shift towards a different career path that aligns "
                                          "more "
                                          "closely with your passions. Your drive and determination are your greatest assets. I see you taking "
                                          "on "
                                          "roles that will challenge you and help you develop new skills. It's important to stay open to "
                                          "learning "
                                          "and be adaptable to change. Your willingness to take on new challenges will lead to substantial "
                                          "professional growth. Networking will play a crucial role in your success. Building strong "
                                          "relationships "
                                          "and connections within your industry will open doors and present new opportunities. Don’t hesitate "
                                          "to "
                                          "seek mentorship and guidance from those who have walked the path before you. Financially, you are "
                                          "on a "
                                          "path to stability and prosperity. Be mindful of your financial decisions and consider investing "
                                          "in your "
                                          "future, whether through further education, training, or strategic investments. Your efforts will "
                                          "pay "
                                          "off, leading to a secure and rewarding career. Overall, your career fortune looks bright and full "
                                          "of "
                                          "potential. Embrace the changes, trust in your abilities, and continue to pursue your goals with "
                                          "passion "
                                          "and determination. Your hard work and perseverance will lead you to a successful and fulfilling "
                                          "career.")
                              else:
                                    answer = ("I sense a dynamic and ambitious energy surrounding your career path. The coming years hold exciting "
                                          "and "
                                          "transformative opportunities for you. Your career fortune is filled with potential and promise. You "
                                          "are "
                                          "on the brink of significant changes and breakthroughs. Within the next year or two, you may "
                                          "encounter "
                                          "pivotal opportunities that could significantly advance your career. This might come in the form of"
                                          " a "
                                          "promotion, a new job offer, or even a chance to pivot to a different field that better aligns with "
                                          "your passions and skills. Your natural talents and hard work will be key drivers of your success. "
                                          "You possess qualities such as resilience, creativity, and determination, which will help you "
                                          "overcome "
                                          "any challenges and seize new opportunities. It’s important to stay adaptable and open to learning "
                                          "new "
                                          "things, as these will be crucial for your growth.")
                        elif age >= "30":
                              answer = ("I sense a strong and mature energy surrounding your career path, indicative of the experiences and "
                                    "wisdom you have accumulated over the years. Your career fortune holds promising developments that "
                                    "will bring both stability and new opportunities for growth. You are entering a period where your hard "
                                    "work and dedication will start to bear significant fruit. Within the next 1 to 3 years, you may "
                                    "encounter opportunities that could lead to a promotion, a significant project, or a leadership role. "
                                    "This is a time to leverage your skills and experiences to advance in your career. Your expertise and "
                                    "confidence will be your greatest assets. You have a deep well of knowledge and skills that you can "
                                    "draw upon to navigate any challenges that come your way. It’s important to continue honing these "
                                    "skills and staying updated with industry trends to remain competitive and innovative. Networking "
                                    "remains crucial at this stage of your career. Building and maintaining strong professional "
                                    "relationships will open doors to new opportunities and collaborations. Seek out mentors and "
                                    "peers who can provide guidance and support, and be open to mentoring others as well. Financially, "
                                    "your prospects look positive. Your past efforts have laid a strong foundation, and with careful "
                                    "planning and strategic investments, you will achieve greater financial security and growth. "
                                    "Consider seeking advice from financial experts to maximize your wealth-building potential. Overall, "
                                    "your career fortune is filled with potential for stability, growth, and fulfillment. Embrace the "
                                    "opportunities that come your way, trust in your abilities, and continue to pursue your professional "
                                    "goals with passion and determination. Your experience and perseverance will lead to a successful and "
                                    "rewarding career.")
            elif question == "2":
                  if gender == "male":
                              if age < "30":
                                    answer = ("haha, nothing")
                              elif age >= "30":
                                    answer = ("If you are currently in a relationship, I see an opportunity for growth and strengthening of your "
                                          "bond. This may involve overcoming challenges together and developing a deeper understanding and "
                                          "appreciation for each other. Communication and honesty will be key in navigating this period, "
                                          "helping you to build a more solid and harmonious partnership. If you are single, your love life "
                                          "is on the brink of positive changes. Within the next year or so, you may meet someone who aligns "
                                          "closely with your values and aspirations. This new connection could come through social events, "
                                          "mutual friends, or even unexpected encounters. Stay open and receptive to new experiences and be "
                                          "confident in expressing your true self.")
                  else:
                              answer = ("I sense a vibrant and loving energy surrounding your romantic life. The coming months and years hold "
                                    "exciting possibilities for deepening connections and finding true fulfillment in your love life. If "
                                    "you are currently in a relationship, I see opportunities for growth and strengthening of your bond. "
                                    "This may involve working through challenges together and fostering a deeper understanding and "
                                    "appreciation for each other. Open and honest communication will be essential in nurturing a harmonious "
                                    "and supportive partnership. If you are single, your love life is poised for positive changes. Within "
                                    "the next year, there is a strong possibility of meeting someone who resonates deeply with your values "
                                    "and desires. This new connection could come through social activities, mutual friends, or even "
                                    "unexpected encounters. Be open to new experiences and trust your instincts when it comes to matters "
                                    "of the heart. Your experiences and personal growth have given you a clear sense of what you seek in "
                                    "a relationship. Use this wisdom to make mindful choices in your romantic pursuits. It's important to "
                                    "stay true to yourself and be patient, as the right person will enter your life when the time is right. "
                                    "Overall, your love life looks promising, with potential for joy, companionship, and lasting connections."
                                    "Embrace the journey with an open heart, and continue to be genuine and authentic in your interactions. "
                                    "Love is on the horizon, bringing warmth, happiness, and fulfillment into your life.")
            elif question == "3":
                  if age < "30":
                        answer = ("I sense a bright and promising future ahead for you, filled with financial success and abundance. "
                              "While the journey may have its ups and downs, your determination, ambition, and talents will pave the "
                              "way for prosperity. As you continue to grow and develop, opportunities will present themselves that "
                              "align with your skills and passions. Stay focused on your goals, and be open to new possibilities "
                              "that may come your way. Trust in your abilities and believe in your capacity to achieve greatness. "
                              "Remember that financial success is not just about the money you earn, but also about how you manage "
                              "and invest it wisely. Take the time to learn about financial planning and make sound decisions that "
                              "will secure your future. Your willingness to work hard, adapt to challenges, and seize opportunities "
                              "will lead to financial stability and success beyond your wildest dreams. Trust in the universe to "
                              "guide you and know that abundance is already on its way to you.")
                  if age >= "30":
                        answer = ("I sense a mature and focused energy surrounding your financial future. The experiences and wisdom you "
                              "have gained over the years have positioned you well for financial success and stability. Your hard work"
                              " and dedication are about to bear significant fruit. In the coming years, you will find opportunities "
                              "that align with your skills and aspirations, leading to increased financial growth and security. This "
                              "may come in the form of career advancements, new ventures, or strategic investments. It’s important "
                              "to continue making informed and prudent financial decisions. Consider seeking advice from financial "
                              "experts or mentors who can help guide you in maximizing your wealth and securing your financial future. "
                              "Diversifying your income streams and investments will also play a crucial role in your financial "
                              "success. Your perseverance and resilience are your greatest assets. Trust in your ability to navigate "
                              "any challenges that come your way. Stay focused on your goals and be open to new opportunities for "
                              "growth and improvement. Overall, your financial outlook is positive. With continued effort, wise "
                              "decision-making, and the right opportunities, you are well on your way to achieving the financial "
                              "success you desire. Embrace this journey with confidence and optimism, knowing that your hard work "
                              "will lead to a prosperous and secure future.")
            elif question == "4":
                  if gender == "male":
                        if age < "30":
                              answer = ("Your personal life will also see significant transformations. This is a time for "
                                    "self-discovery and personal development. You may find yourself exploring new hobbies, "
                                    "interests, or even considering further education. These pursuits will help you understand "
                                    "yourself better and define your goals more clearly."
                                    "Important changes in your relationships are on the horizon. This could mean deepening "
                                    "existing relationships or forming new, meaningful connections. Be open to meeting new "
                                    "people and nurturing the bonds that matter most to you. These relationships will provide "
                                    "support and enrich your life."
                                    "There is a strong possibility of relocation or travel. This might be due to career "
                                    "opportunities, personal decisions, or a desire for new experiences. Such changes will "
                                    "broaden your horizons and offer new perspectives.")
                        elif age >= "30":
                              answer = ("You are likely to experience important developments in your professional life. This might "
                                    "include a career advancement, a new job offer, or even a complete career change. These "
                                    "shifts will bring new challenges and opportunities for growth. Embrace them, as they will "
                                    "lead to greater professional satisfaction and success."
                                    "Your personal life will also undergo positive changes. You may find yourself pursuing new "
                                    "interests or rekindling old passions. This period is ideal for personal growth and "
                                    "self-discovery. Consider taking up new hobbies, furthering your education, or exploring "
                                    "creative outlets that bring you joy and fulfillment."
                                    "Paying attention to your health and well-being will become increasingly important. "
                                    "You may decide to make lifestyle changes that improve your physical and mental health. "
                                    "Regular exercise, a balanced diet, and mindfulness practices will greatly benefit you "
                                    "during this time of transition.")
            else:
                        if age < "30":
                              answer = ("Significant changes in your personal relationships are likely. You may deepen existing "
                                    "bonds, form new friendships, or even meet a romantic partner who has a profound impact "
                                    "on your life. Focus on nurturing your connections and being open to new relationships "
                                    "that bring joy and support."
                                    "Positive shifts in your financial situation are expected. This could involve finding "
                                    "new income sources, improving your financial management skills, or making smart "
                                    "investments. Be mindful of your financial decisions and seek advice when necessary "
                                    "to build a secure and prosperous future."
                                    "You may experience significant changes in your living situation or lifestyle. "
                                    "This could involve moving to a new place, traveling, or making lifestyle adjustments "
                                    "that align with your evolving goals and values. Embrace these changes as they will bring "
                                    "fresh perspectives and new experiences.")
                        elif age >= "30":
                              answer = ("You are on the verge of a journey of self-discovery and personal reinvention. This "
                                    "might involve pursuing new hobbies, furthering your education, or embarking on creative "
                                    "projects. These activities will bring you joy and a deeper sense of purpose. Trust your "
                                    "intuition and follow your passions."
                                    "Your health and well-being will take center stage. This is a time to adopt healthier "
                                    "lifestyle habits, whether through regular exercise, a balanced diet, or mindfulness "
                                    "practices. These changes will enhance your physical vitality and mental clarity, "
                                    "allowing you to enjoy life to the fullest."
                                    "Changes in your living environment or lifestyle are possible. This could mean "
                                    "moving to a new home, renovating your current space, or making other adjustments "
                                    "that better reflect your needs and desires. These changes will bring a fresh "
                                    "perspective and rejuvenate your daily life.")

      return jsonify(answer=answer)

if __name__ == '__main__':
     app.run(debug=True)