from crewai import Task


def task_to_strings(task: Task):
    """Convert a Task object into (task, context) strings for DelegateWorkTool."""
    return (
        task.description.strip(),
        f"Expected output:\n{task.expected_output.strip()}" if task.expected_output else ""
    )


# -----------------------------
#  Teaching Task
# -----------------------------
def teaching_task(topic, skill_level, context="", student_background=""):
    return Task(
        description=f"""
        You are responsible for teaching the C++ topic **'{topic}'** to a {skill_level} student.

        CONTEXT FROM PREVIOUS CONVERSATION:
        {context}

        STUDENT PROFILE:
        - Skill Level: {skill_level}
        - Background: {student_background if student_background else 'Not provided'}
        - Specific Request: "{topic}"

        REQUIREMENTS:
        1. Provide a COMPREHENSIVE explanation, not just an introduction
        2. Start with a simple and clear definition of the topic
        3. Provide a relatable analogy that connects to everyday life
        4. Create 3-5 progressively complex C++ code examples that build understanding step-by-step
        5. Highlight common mistakes and misconceptions learners often make with this topic
        6. Provide practical applications (real-world uses, mini-projects)
        7. Share memory tips or strategies to help the student retain the concept
        8. Include practice exercises with solutions
        9. Adjust the technical depth to match the student's {skill_level} level
        10. DO NOT use external search tools - rely on your own knowledge
        11. DO NOT ask the student what they want to know - provide a complete explanation
        12. Cover all fundamental aspects of the topic in a structured manner

        IMPORTANT: Provide a complete, standalone explanation. Do not suggest external resources or tell the student to search elsewhere.
        IMPORTANT: Consider the conversation context to maintain continuity and avoid repeating information.
        IMPORTANT: Never end your explanation with a question asking what the student wants to know next.

        TONE & STYLE:
        - Use plain, beginner-friendly language (avoid unnecessary jargon)
        - If a technical term must be used, define it clearly
        - Keep explanations engaging and supportive
        - Provide full explanations, not just introductory statements
        - Reference previous conversation when appropriate to maintain continuity
        """,
        expected_output=f"""
        A comprehensive educational guide (Markdown format) that includes:
        - A clear title with the topic name
        - A detailed definition of the topic
        - An analogy that relates to everyday life
        - 3-5 progressive code examples with explanations
        - A section on common mistakes and how to avoid them
        - A section on practical applications with real-world examples
        - Practice exercises with solutions
        - A section with memory tips and learning strategies
        - A summary and next learning steps

        The guide should be thorough enough that a student could read it and have a solid understanding
        of the topic, not just a superficial introduction. It should also maintain continuity with
        previous conversation when appropriate.

        CRITICAL: The explanation must be complete and self-contained. Do not end with questions
        asking what the student wants to know next.
        """,
        agent=None,
        output_file='teaching_report.md',
        config={},
    )


# -----------------------------
#  Code Review Task
# -----------------------------
def code_review_task(code_snippet, skill_level, context="", specific_concerns=""):
    return Task(
        description=f"""
        You are reviewing the following C++ code for a **{skill_level}** level student:

        CONTEXT FROM PREVIOUS CONVERSATION:
        {context}

        CODE TO REVIEW:
        ```cpp
        {code_snippet}
        ```

        Specific Concerns: {specific_concerns if specific_concerns else 'None provided'}

        REQUIREMENTS:
        1. Check **syntax and structure** for correctness.
        2. Evaluate **logic and efficiency**.
        3. Review **coding standards compliance** (readability, naming conventions, formatting).
        4. Assess **memory management and pointer usage** (if applicable).
        5. Identify opportunities to improve **readability and maintainability**.
        6. Provide **specific, actionable suggestions** for improvements.
        7. For each issue:
           - Explain why it's problematic.
           - Show the corrected code.
           - Explain why the correction improves the code.
        8. Provide a **final corrected version** of the full code.
        9. Consider the conversation context to provide relevant feedback.
        10. Provide a comprehensive review, not just quick tips.

        TONE & STYLE:
        - Be constructive and encouraging (don't overwhelm the student).
        - Explanations should be tailored for a **{skill_level}** student.
        - Prioritize the most important issues first.
        - Reference previous conversation when appropriate to maintain continuity.
        - Provide detailed explanations, not just brief comments.
        """,
        expected_output="""
        A structured code review (Markdown format) with:
        - **Overall assessment** (summary of strengths & weaknesses).
        - **Section-by-section analysis**.
        - A list of **issues with explanations**.
        - **Corrected code snippets** for each issue.
        - A **final corrected full code version**.
        - A list of **recommended resources** for further learning.
        - Continuity with previous conversation when relevant.

        The review should be comprehensive and educational, not just a quick checklist.
        """,
        agent=None,
        output_file='code_review.md',
        config={},
    )


# -----------------------------
#  Curriculum Design Task
# -----------------------------
def curriculum_task(student_goals, current_level, time_availability, context="", specific_interests=""):
    return Task(
        description=f"""
        Design a personalized **C++ learning curriculum**.

        CONTEXT FROM PREVIOUS CONVERSATION:
        {context}

        STUDENT PROFILE:
        - Current Skill Level: {current_level}
        - Goals: {student_goals}
        - Time Availability: {time_availability}
        - Specific Interests: {specific_interests if specific_interests else 'Not provided'}

        REQUIREMENTS:
        1. Provide an **overall learning roadmap** with milestones.
        2. Break down the roadmap into **time-based segments** (weekly or monthly).
        3. Specify **topics to cover in each period**.
        4. Recommend **resources** (books, tutorials, documentation, videos).
        5. Assign **practice projects** for each major milestone.
        6. Include **assessment checkpoints** to track progress.
        7. Suggest strategies for **overcoming common learning plateaus**.
        8. Ensure the timeline is realistic for the given **{time_availability}**.
        9. Consider the conversation context to tailor the curriculum appropriately.
        10. Create a detailed, actionable plan, not just general advice.

        TONE & STYLE:
        - Curriculum should balance **theory and practice**.
        - Recommend projects that match **student interests**.
        - Keep the plan **realistic and motivating**.
        - Reference previous conversation when appropriate to maintain continuity.
        - Provide specific recommendations, not vague suggestions.
        """,
        expected_output="""
        A detailed learning plan (Markdown format) with:
        - **Overview** of the journey.
        - **Timeline** (weeks/months).
        - **Topics** for each period.
        - **Resources** for each topic.
        - **Practice projects** with descriptions.
        - **Assessment checkpoints**.
        - **Motivation tips** and advice for plateaus.
        - Continuity with previous conversation when relevant.

        The plan should be comprehensive and specific, with clear actionable steps.
        """,
        agent=None,
        output_file='learning_plan.md',
        config={},
    )


# -----------------------------
#  Quiz Creation Task
# -----------------------------
def quiz_task(topic, skill_level, context="", quiz_type="mixed"):
    return Task(
        description=f"""
        Create a **{quiz_type} quiz** on the topic **'{topic}'**.

        CONTEXT FROM PREVIOUS CONVERSATION:
        {context}

        STUDENT PROFILE:
        - Skill Level: {skill_level}

        REQUIREMENTS:
        1. Include **5-8 questions** of varying difficulty.
        2. Use a mix of question types:
           - Multiple choice
           - Code output prediction
           - Bug identification
        3. Ensure questions are **clear and unambiguous**.
        4. For multiple choice:
           - Provide **plausible distractors**.
        5. Provide **detailed explanations** for correct answers.
        6. Explain **why incorrect answers are wrong**.
        7. Include a **scoring system or performance guide**.
        8. Consider the conversation context to tailor quiz difficulty and content.
        9. Create a comprehensive assessment, not just a few quick questions.

        TONE & STYLE:
        - Keep questions **educational, not tricky**.
        - Match difficulty to **{skill_level}**.
        - Focus on **conceptual understanding** rather than rote memorization.
        - Reference previous conversation when appropriate to maintain continuity.
        - Provide thorough explanations for all answers.
        """,
        expected_output="""
        A complete quiz (Markdown format) with:
        - **Title and instructions**.
        - Well-formatted **questions**.
        - **Answer choices** where relevant.
        - **Answer key with explanations**.
        - **Scoring guidelines**.
        - **Study recommendations** based on performance.
        - Continuity with previous conversation when relevant.

        The quiz should be comprehensive and educational, with detailed explanations for all answers.
        """,
        agent=None,
        output_file='quiz.md',
        config={},
    )


# -----------------------------
#  Coordination Task
# -----------------------------
def coordination_task(context, student_query, student_level, student_goals):
    # Make sure context is always turned into a readable string
    if isinstance(context, list):
        context_str = "\n".join(context)
    else:
        context_str = str(context)

    return Task(
        description=f"""
        Coordinate the learning experience for a student with these characteristics:

        - Current query: {student_query}
        - Skill level: {student_level}
        - Learning goals: {student_goals}

        CONVERSATION CONTEXT:
        {context_str}

        Your responsibilities:
        1. Decide which specialist agent(s) should handle this request.
        2. Assign specific tasks to each relevant agent.
        3. Maintain continuity with previous learning sessions.
        4. Ensure a cohesive and personalized learning experience.
        5. Synthesize multiple specialists' outputs if necessary.
        6. Consider the full conversation history to provide the most relevant response.
        7. Ensure the student receives comprehensive explanations, not just brief answers.

        IMPORTANT: If the student asks about a technical topic, delegate to the teaching expert
        for a comprehensive explanation. Do not provide short answers yourself.
        """,
        expected_output="""
        A coordination plan that includes:
        - Analysis of the student's query and needs
        - Decision on which specialist(s) to engage
        - Specific tasks to assign to each specialist
        - Context maintenance strategy
        - Plan for synthesizing multiple responses if needed
        - Next steps for the learning journey
        - Continuity with previous conversation
        - Assurance that the student will receive a comprehensive response
        """,
        agent=None,
        output_file="coordination_plan.md",
        config={},
    )


# -----------------------------
#  Conversation Task
# -----------------------------
def conversation_task(user_input, context=""):
    return Task(
        description=f"""
        Handle this casual conversation message from the student: "{user_input}"

        CONTEXT FROM PREVIOUS CONVERSATION:
        {context}

        Your goal is to respond naturally and keep the conversation flowing. This is not a technical 
        question about C++ - it's casual conversation like greetings, thanks, or general chat.

        SPECIAL INSTRUCTIONS FOR TECHNICAL TOPICS:
        - If the student asks about a technical C++ topic, DO NOT attempt to answer it yourself
        - Instead, acknowledge the question and delegate it to the appropriate teaching agent
        - Say something like "That's a great question! Let me explain that in detail..." and then
          let the teaching expert take over with a comprehensive explanation

        SPECIAL INSTRUCTIONS FOR FOLLOW-UPS:
        - If the student says "yes", "please", or "tell me more", gently guide them to ask a specific question
        - If they seem interested in learning more, encourage them to ask about a specific C++ topic
        - Don't provide technical explanations yourself - redirect to proper teaching if needed
        - Use the conversation context to maintain continuity and avoid asking for clarification on topics already discussed

        GUIDELINES:
        1. Keep responses brief and friendly (1-2 sentences max)
        2. Match the tone of the student's message
        3. If they say thanks, acknowledge it warmly
        4. If they greet you, respond appropriately
        5. If they make small talk, engage naturally
        6. Gently steer the conversation back to C++ learning when appropriate
        7. Don't overthink it - keep it simple and human-like
        8. Use the conversation context to maintain continuity
        9. NEVER provide technical explanations - always delegate to teaching experts

        Remember: The student is interacting with a C++ tutor, so keep your responses relevant 
        to the learning context while being natural and conversational.
        """,
        expected_output="A brief, friendly, natural conversation response (1-2 sentences max) that maintains a positive learning environment and continuity with previous conversation. If the message is technical, acknowledge it and delegate to a teaching expert.",
        agent=None,
        output_file='conversation_log.md',
        config={},
    )