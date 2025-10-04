from collections import Counter
import sys

doc = [
    """You are solely responsible for the successes that you gain in your life. In this session Brian provides
    you with insights and direction on how you can take charge of your life and create those successes.
    He targets the greatest enemies to happiness and success as being negative emotions: fear, self-
    pity, envy, jealousy, feelings of inferiority, and ultimately anger. He identifies the four causal factors
    that contribute to negativity as being justification, rationalization, over-concern or hypersensitivity,
    and blaming. To aid you in fully taking charge of your life, Brian suggests that you always see
    yourself as “self-employed,” and that you develop your own strategic plan for your life and career.
    This plan should include making new choices and decisions, becoming a “growth stock,” taking the
    wheel of your own fate, determining your focus of control, and incorporating the golden triangle
    concept into your goal-setting initiatives.""",

    """There are four special qualities that stand out among all great leaders. They have vision, they
    know who they are, what they believe in, and what they stand for. In this session Brian assists
    you in establishing your unique vision as he asks many probing questions about your ideal future.
    He encourages you to suspend any disbelieving thoughts and to take a journey into the world of
    yourself as “self-employed,” and that you develop your own strategic plan for your life and career.
    This plan should include making new choices and decisions, becoming a “growth stock,” taking the
    wheel of your own fate, determining your focus of control, and incorporating the golden triangle
    concept into your goal-setting initiatives.""",

    """There are four special qualities that stand out among all great leaders. They have vision, they
    know who they are, what they believe in, and what they stand for. In this session Brian assists
    you in establishing your unique vision as he asks many probing questions about your ideal future.
    He encourages you to suspend any disbelieving thoughts and to take a journey into the world of
    possibility. Once you have an image of the life that you want, you need to clarify what your inner
    values. In order to do this, Brian encourages you to look within yourself, know yourself, trust your
    intuition, examine your past and present behaviors, determine your level of self-esteem, and finally,
    be sure to live in your truth.""",

    """The next step in establishing your ultimate goals is to determine what you really want to do with the
    rest of your life. In this session Brian aids you in determining what you want, while identifying the
    major worries that may stand in your way. He assists you in creating your dream list by introducing
    the “magic wand,” “six months to live,” and “instant millionaire” scenarios. He further encourages
    you to do what you want to do while making a difference in the world. Once you have decided upon
    your true goals, it is important that you uncover what your major definite purpose is. In doing so,
    you activate the reticular cortex of your brain. This in turn alerts your attention to the people,
    information, and opportunities in your environment that will help you to achieve your goals.""",

    """Your beliefs create your reality. The trick to success is to knowing your current beliefs and how they
    affect you so that you can then select beliefs that will support the kind of life you wish for. In this
    session Brian assists you in ascertaining exactly what your current beliefs are and how to fully and
    consciously commit to your newly selected beliefs. Once you have established this new belief
    system, you are then ready to take your first major action step. Practicing the “reality principle” is
    an invaluable springboard that enables you to evaluate your current life and prepares you for putting
    together your own strategic plan.""",

    """The three keys to peak performance are commitment, completion, and closure. In this session you
    will learn how to measure your progress, focusing on the three keys as your barometer. Brian
    suggests simple and doable tasks that you can accomplish to attain your goals in whatever area of
    your life they may pertain to. He then shares several powerful exercises that you can do to eliminate
    any roadblocks that you may come up against as you work toward your goals.""",

    """Two valuable keys to attaining your goals are to become an expert in your chosen field of endeavor
    and to become involved with the right people. Brian outlines the key assets that you need to acquire
    and continue to develop if you seek to be outstanding in your chosen field. He identifies the seven
    key result areas that determine your success or failure at your job, and he lists the eight ways for
    you to identify and determine your special talents. He stresses that it is imperative that you identify
    and further develop your special talents, along with becoming a relationship expert. He reminds you
    that everything in life and business is relationships. Investing considerable time and effort into
    creating healthy and effective relationships with those that you are in contact with, from your
    customers and employment team to your friends and family members, will prove to be invaluable.""",

    """Brian opens this session by clarifying the difference between “positive thinking” and “positive
    knowing.” He stresses the significance of programming your subconscious mind and actually
    “knowing” that you are destined for success. It is important that you systematically set your goals
    and discipline yourself to writing them down each day. He suggests several tools that you can use to
    most effectively create and update your goals. He then discusses the power that lies in your ability
    to constantly visualize your goals. He lists the four parts of visualization that you can learn and
    practice to ensure that you use this awesome power to its best advantage: frequency, duration,
    vividness, and intensity.""",

    """In this session Brian introduces the superconscious mind as a powerful ally in your goal-setting
    strategies. He discusses the conditions in which you can best activate it, and he describes how it
    functions in conjunction with the goal-setting steps that you have already taken. The two ways that
    you can stimulate it are by concentrating and working intensely on achieving your goal and by
    relaxing completely and getting your mind busy elsewhere. He emphasizes that the more you trust
    the capacity of your superconscious mind, the greater its power will be. Another key to achieving
    your goals is to remain flexible. At times when there is rapid change, flexibility has been cited as the
    single most important quality that you can develop. Brian lists the many areas in which you need to
    remain flexible, alert, and open as you begin to manifest your goals. He gives you three valuable
    statements you learn to say to remain flexible during turbulent times: 1) “I was wrong.” 2) “I made a
    mistake.” 3) “I changed my mind.""",

    """Your creativity and brainpower are like muscles that constantly have to be stretched and used in
    order to be fully effective. Brian illustrates the capacity that we all have for greater creativity, and
    he provides you with many tools that you can use to improve your “creative genius” muscle. He also
    outlines ways in which you can ward off potentially destructive challenges that may come your way.
    He then lists a four-step problem-solving methodology that you can and should use as you continue
    on your goal-achieving journey: Step 1: Define the problem clearly. Step 2: Ask, “What are all the
    possible causes of this problem?” Step 3: Ask, “What are all the possible solutions?” Step 4: Once
    you have identified several possible solutions, ask, “What must this solution accomplish?” He ends
    this session by discussing the importance of taking some action toward your goals every day.
    Consistency and commitment are key."""
]

print(len(doc))
entire_doc = "\n".join(doc)
words = entire_doc.lower().split()
stop_words = ['your', 'you', 'a', 'for', "'s", 'to', 'and', 'that', 'the', 'in', 'of', 'he', 'brian', 'what', 'are', 'in', 'this', 'as', 'is', 'with']
words = [word for word in words if word not in stop_words]

words_c = Counter(words)
my_words = ['life', 'goals', 'determine', 'encourages', 'develop', 'choices', 'success', 'special', 'need', 'important', 'create', 'mind', 'power']

for para in doc:
    print("-" * 20)
    lower_para = para.lower()
    for word in my_words:
        print(word, "-", lower_para.count(word))
    sys.stdout.flush()  # Only keep this for VS Code compatibility
