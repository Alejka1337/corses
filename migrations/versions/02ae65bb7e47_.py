"""empty message

Revision ID: 02ae65bb7e47
Revises: 
Create Date: 2024-03-20 17:50:53.541154

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '02ae65bb7e47'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('image_path', sa.String(), nullable=True),
    sa.Column('discount', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_index(op.f('ix_categories_id'), 'categories', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('usertype', sa.Enum('student', 'moder', name='usertype'), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('access_token', sa.String(), nullable=True),
    sa.Column('refresh_token', sa.String(), nullable=True),
    sa.Column('hashed_pass', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('exp_token', sa.DateTime(), nullable=True),
    sa.Column('last_active', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_table('activate_codes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    op.create_index(op.f('ix_activate_codes_id'), 'activate_codes', ['id'], unique=False)
    op.create_table('courses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('image_path', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('old_price', sa.Float(), nullable=True),
    sa.Column('is_published', sa.Boolean(), nullable=False),
    sa.Column('quantity_lecture', sa.Integer(), nullable=True),
    sa.Column('quantity_test', sa.Integer(), nullable=True),
    sa.Column('c_type', sa.String(), nullable=True),
    sa.Column('c_duration', sa.String(), nullable=True),
    sa.Column('c_award', sa.String(), nullable=True),
    sa.Column('c_language', sa.String(), nullable=True),
    sa.Column('c_level', sa.String(), nullable=True),
    sa.Column('c_access', sa.String(), nullable=True),
    sa.Column('intro_text', sa.String(), nullable=False),
    sa.Column('skills_text', sa.String(), nullable=False),
    sa.Column('about_text', sa.String(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_index(op.f('ix_courses_id'), 'courses', ['id'], unique=False)
    op.create_table('images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('path', sa.String(), nullable=False),
    sa.Column('is_main', sa.Boolean(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_images_id'), 'images', ['id'], unique=False)
    op.create_table('instructions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('type', sa.Enum('general', 'course', name='instructiontype'), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('last_update', sa.DateTime(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_instructions_id'), 'instructions', ['id'], unique=False)
    op.create_table('moderators',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('surname', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('country', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone')
    )
    op.create_index(op.f('ix_moderators_id'), 'moderators', ['id'], unique=False)
    op.create_table('reset_password_links',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('link', sa.String(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('link')
    )
    op.create_index(op.f('ix_reset_password_links_id'), 'reset_password_links', ['id'], unique=False)
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('surname', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('country', sa.String(), nullable=True),
    sa.Column('balance', sa.Integer(), nullable=False),
    sa.Column('studying_time', sa.Integer(), nullable=False),
    sa.Column('changed_name', sa.Boolean(), nullable=False),
    sa.Column('changed_surname', sa.Boolean(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.CheckConstraint('balance >= 0', name='positive_balance'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone')
    )
    op.create_index(op.f('ix_students_id'), 'students', ['id'], unique=False)
    op.create_table('category_certificates',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('link', sa.String(), nullable=False),
    sa.Column('addition_link', sa.String(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_category_certificates_id'), 'category_certificates', ['id'], unique=False)
    op.create_table('chat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('chat_subject', sa.String(), nullable=False),
    sa.Column('status', sa.Enum('new', 'active', 'archive', name='chatstatustype'), nullable=False),
    sa.Column('initiator_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['initiator_id'], ['students.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_chat_id'), 'chat', ['id'], unique=False)
    op.create_table('course_certificates',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('link', sa.String(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_course_certificates_id'), 'course_certificates', ['id'], unique=False)
    op.create_table('course_icons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('icon_path', sa.String(), nullable=False),
    sa.Column('icon_number', sa.Integer(), nullable=False),
    sa.Column('icon_title', sa.String(), nullable=False),
    sa.Column('icon_text', sa.String(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_course_icons_id'), 'course_icons', ['id'], unique=False)
    op.create_table('instruction_files',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('file_type', sa.String(), nullable=False),
    sa.Column('file_name', sa.String(), nullable=False),
    sa.Column('file_path', sa.String(), nullable=False),
    sa.Column('file_size', sa.Integer(), nullable=False),
    sa.Column('instruction_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['instruction_id'], ['instructions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_instruction_files_id'), 'instruction_files', ['id'], unique=False)
    op.create_table('lessons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.Enum('lecture', 'test', 'exam', name='lessontype'), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('is_published', sa.Boolean(), nullable=False),
    sa.Column('scheduled_time', sa.Integer(), nullable=True),
    sa.Column('image_path', sa.String(), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_lessons_id'), 'lessons', ['id'], unique=False)
    op.create_table('student_course_association',
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('grade', sa.Integer(), nullable=False),
    sa.Column('progress', sa.Integer(), nullable=False),
    sa.Column('status', sa.Enum('completed', 'in_progress', name='coursestatus'), nullable=False),
    sa.CheckConstraint('grade <= 200', name='grade_less_then_200'),
    sa.CheckConstraint('progress <= 100', name='progress_less_then_100_present'),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.PrimaryKeyConstraint('student_id', 'course_id')
    )
    op.create_index(op.f('ix_student_course_association_course_id'), 'student_course_association', ['course_id'], unique=False)
    op.create_index(op.f('ix_student_course_association_student_id'), 'student_course_association', ['student_id'], unique=False)
    op.create_table('user_folders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('parent_id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['parent_id'], ['user_folders.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_folders_id'), 'user_folders', ['id'], unique=False)
    op.create_table('chat_messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('chat_id', sa.Integer(), nullable=False),
    sa.Column('sender_id', sa.Integer(), nullable=False),
    sa.Column('sender_type', sa.Enum('student', 'admin', name='messagesendertype'), nullable=False),
    sa.Column('recipient_id', sa.Integer(), nullable=True),
    sa.Column('recipient_type', sa.Enum('student', 'admin', name='messagesendertype'), nullable=False),
    sa.ForeignKeyConstraint(['chat_id'], ['chat.id'], ),
    sa.ForeignKeyConstraint(['recipient_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['sender_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_chat_messages_id'), 'chat_messages', ['id'], unique=False)
    op.create_table('exams',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=False),
    sa.Column('min_score', sa.Integer(), nullable=True),
    sa.Column('attempts', sa.Integer(), nullable=False),
    sa.Column('timer', sa.Integer(), nullable=False),
    sa.Column('lesson_id', sa.Integer(), nullable=False),
    sa.CheckConstraint('score <= 200', name='check_score_less_than_200'),
    sa.CheckConstraint('score > 0', name='check_score_more_than_0'),
    sa.ForeignKeyConstraint(['lesson_id'], ['lessons.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_exams_id'), 'exams', ['id'], unique=False)
    op.create_table('lectures',
    sa.Column('audios', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lesson_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['lesson_id'], ['lessons.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_lectures_id'), 'lectures', ['id'], unique=False)
    op.create_table('student_lessons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.Enum('completed', 'active', 'blocked', 'new', name='lessonstatus'), nullable=False),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('attempt', sa.Integer(), nullable=True),
    sa.Column('lesson_id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['lesson_id'], ['lessons.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_student_lessons_id'), 'student_lessons', ['id'], unique=False)
    op.create_table('tests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=False),
    sa.Column('attempts', sa.Integer(), nullable=False),
    sa.Column('lesson_id', sa.Integer(), nullable=False),
    sa.CheckConstraint('score <= 200', name='check_score_less_than_200'),
    sa.CheckConstraint('score > 0', name='check_score_more_than_0'),
    sa.ForeignKeyConstraint(['lesson_id'], ['lessons.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tests_id'), 'tests', ['id'], unique=False)
    op.create_table('exam_questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('q_text', sa.String(), nullable=False),
    sa.Column('q_number', sa.Integer(), nullable=False),
    sa.Column('q_score', sa.Integer(), nullable=False),
    sa.Column('q_type', sa.Enum('test', 'boolean', 'answer_with_photo', 'question_with_photo', 'matching', 'multiple_choice', name='questiontypeoption'), nullable=False),
    sa.Column('hidden', sa.Boolean(), nullable=False),
    sa.Column('image_path', sa.String(), nullable=True),
    sa.Column('exam_id', sa.Integer(), nullable=False),
    sa.CheckConstraint('q_number > 0', name='check_q_number_positive'),
    sa.CheckConstraint('q_score <= 200', name='check_q_score_less_than_200'),
    sa.CheckConstraint('q_score > 0', name='check_q_score_more_than_0'),
    sa.ForeignKeyConstraint(['exam_id'], ['exams.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_exam_questions_id'), 'exam_questions', ['id'], unique=False)
    op.create_table('lecture_attributes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('a_type', sa.Enum('text', 'present', 'audio', 'picture', 'video', 'file', 'link', name='lectureattributetype'), nullable=False),
    sa.Column('a_title', sa.String(), nullable=False),
    sa.Column('a_number', sa.Integer(), nullable=False),
    sa.Column('a_text', sa.String(), nullable=True),
    sa.Column('hidden', sa.Boolean(), nullable=False),
    sa.Column('lecture_id', sa.Integer(), nullable=False),
    sa.CheckConstraint('a_number > 0', name='check_a_number_positive'),
    sa.ForeignKeyConstraint(['lecture_id'], ['lectures.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_lecture_attributes_id'), 'lecture_attributes', ['id'], unique=False)
    op.create_table('message_files',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('file_type', sa.String(), nullable=False),
    sa.Column('file_name', sa.String(), nullable=False),
    sa.Column('file_path', sa.String(), nullable=False),
    sa.Column('file_size', sa.Integer(), nullable=False),
    sa.Column('message_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['message_id'], ['chat_messages.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_message_files_id'), 'message_files', ['id'], unique=False)
    op.create_table('student_exam_attempts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('attempt_number', sa.Integer(), nullable=False),
    sa.Column('attempt_score', sa.Integer(), nullable=False),
    sa.Column('exam_id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['exam_id'], ['exams.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_student_exam_attempts_id'), 'student_exam_attempts', ['id'], unique=False)
    op.create_table('student_test_attempts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('attempt_number', sa.Integer(), nullable=False),
    sa.Column('attempt_score', sa.Integer(), nullable=False),
    sa.Column('test_id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.ForeignKeyConstraint(['test_id'], ['tests.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_student_test_attempts_id'), 'student_test_attempts', ['id'], unique=False)
    op.create_table('test_questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('q_text', sa.String(), nullable=False),
    sa.Column('q_number', sa.Integer(), nullable=False),
    sa.Column('q_score', sa.Integer(), nullable=False),
    sa.Column('q_type', sa.Enum('test', 'boolean', 'answer_with_photo', 'question_with_photo', 'matching', 'multiple_choice', name='questiontypeoption'), nullable=False),
    sa.Column('hidden', sa.Boolean(), nullable=False),
    sa.Column('image_path', sa.String(), nullable=True),
    sa.Column('test_id', sa.Integer(), nullable=False),
    sa.CheckConstraint('q_number > 0', name='check_q_number_positive'),
    sa.CheckConstraint('q_score <= 200', name='check_q_score_less_than_200'),
    sa.CheckConstraint('q_score > 0', name='check_q_score_more_than_0'),
    sa.ForeignKeyConstraint(['test_id'], ['tests.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_test_questions_id'), 'test_questions', ['id'], unique=False)
    op.create_table('user_notes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('folder_id', sa.Integer(), nullable=False),
    sa.Column('lecture_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['folder_id'], ['user_folders.id'], ),
    sa.ForeignKeyConstraint(['lecture_id'], ['lectures.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_notes_id'), 'user_notes', ['id'], unique=False)
    op.create_table('exam_answers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('a_text', sa.String(), nullable=False),
    sa.Column('is_correct', sa.Boolean(), nullable=False),
    sa.Column('image_path', sa.String(), nullable=True),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['exam_questions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_exam_answers_id'), 'exam_answers', ['id'], unique=False)
    op.create_table('exam_matching_right',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['exam_questions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_exam_matching_right_id'), 'exam_matching_right', ['id'], unique=False)
    op.create_table('lecture_files',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('filename', sa.String(), nullable=False),
    sa.Column('file_path', sa.String(), nullable=False),
    sa.Column('file_size', sa.Integer(), nullable=False),
    sa.Column('file_description', sa.String(), nullable=True),
    sa.Column('download_allowed', sa.Boolean(), nullable=True),
    sa.Column('attribute_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['attribute_id'], ['lecture_attributes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_lecture_files_id'), 'lecture_files', ['id'], unique=False)
    op.create_table('lecture_links',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('link', sa.String(), nullable=False),
    sa.Column('anchor', sa.String(), nullable=True),
    sa.Column('attribute_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['attribute_id'], ['lecture_attributes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_lecture_links_id'), 'lecture_links', ['id'], unique=False)
    op.create_table('student_exam_answers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('question_type', sa.Enum('test', 'boolean', 'answer_with_photo', 'question_with_photo', 'matching', 'multiple_choice', name='questiontypeoption'), nullable=False),
    sa.Column('answer_id', sa.Integer(), nullable=True),
    sa.Column('answer_ids', sa.ARRAY(sa.Integer()), nullable=True),
    sa.Column('student_attempt_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['exam_questions.id'], ),
    sa.ForeignKeyConstraint(['student_attempt_id'], ['student_exam_attempts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_student_exam_answers_id'), 'student_exam_answers', ['id'], unique=False)
    op.create_table('student_test_answers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('question_type', sa.Enum('test', 'boolean', 'answer_with_photo', 'question_with_photo', 'matching', 'multiple_choice', name='questiontypeoption'), nullable=False),
    sa.Column('answer_id', sa.Integer(), nullable=True),
    sa.Column('answer_ids', sa.ARRAY(sa.Integer()), nullable=True),
    sa.Column('student_attempt_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['test_questions.id'], ),
    sa.ForeignKeyConstraint(['student_attempt_id'], ['student_test_attempts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_student_test_answers_id'), 'student_test_answers', ['id'], unique=False)
    op.create_table('test_answers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('a_text', sa.String(), nullable=False),
    sa.Column('is_correct', sa.Boolean(), nullable=False),
    sa.Column('image_path', sa.String(), nullable=True),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['test_questions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_test_answers_id'), 'test_answers', ['id'], unique=False)
    op.create_table('test_matching_right',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['test_questions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_test_matching_right_id'), 'test_matching_right', ['id'], unique=False)
    op.create_table('exam_matching_left',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('right_id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['exam_questions.id'], ),
    sa.ForeignKeyConstraint(['right_id'], ['exam_matching_right.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_exam_matching_left_id'), 'exam_matching_left', ['id'], unique=False)
    op.create_table('test_matching_left',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('right_id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['test_questions.id'], ),
    sa.ForeignKeyConstraint(['right_id'], ['test_matching_right.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_test_matching_left_id'), 'test_matching_left', ['id'], unique=False)
    op.create_table('student_exam_matching',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('question_type', sa.Enum('test', 'boolean', 'answer_with_photo', 'question_with_photo', 'matching', 'multiple_choice', name='questiontypeoption'), nullable=False),
    sa.Column('left_id', sa.Integer(), nullable=False),
    sa.Column('right_id', sa.Integer(), nullable=False),
    sa.Column('student_attempt_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['left_id'], ['exam_matching_left.id'], ),
    sa.ForeignKeyConstraint(['question_id'], ['exam_questions.id'], ),
    sa.ForeignKeyConstraint(['right_id'], ['exam_matching_right.id'], ),
    sa.ForeignKeyConstraint(['student_attempt_id'], ['student_exam_attempts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_student_exam_matching_id'), 'student_exam_matching', ['id'], unique=False)
    op.create_table('student_test_matching',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('question_type', sa.Enum('test', 'boolean', 'answer_with_photo', 'question_with_photo', 'matching', 'multiple_choice', name='questiontypeoption'), nullable=False),
    sa.Column('left_id', sa.Integer(), nullable=False),
    sa.Column('right_id', sa.Integer(), nullable=False),
    sa.Column('student_attempt_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['left_id'], ['test_matching_left.id'], ),
    sa.ForeignKeyConstraint(['question_id'], ['test_questions.id'], ),
    sa.ForeignKeyConstraint(['right_id'], ['test_matching_right.id'], ),
    sa.ForeignKeyConstraint(['student_attempt_id'], ['student_test_attempts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_student_test_matching_id'), 'student_test_matching', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_student_test_matching_id'), table_name='student_test_matching')
    op.drop_table('student_test_matching')
    op.drop_index(op.f('ix_student_exam_matching_id'), table_name='student_exam_matching')
    op.drop_table('student_exam_matching')
    op.drop_index(op.f('ix_test_matching_left_id'), table_name='test_matching_left')
    op.drop_table('test_matching_left')
    op.drop_index(op.f('ix_exam_matching_left_id'), table_name='exam_matching_left')
    op.drop_table('exam_matching_left')
    op.drop_index(op.f('ix_test_matching_right_id'), table_name='test_matching_right')
    op.drop_table('test_matching_right')
    op.drop_index(op.f('ix_test_answers_id'), table_name='test_answers')
    op.drop_table('test_answers')
    op.drop_index(op.f('ix_student_test_answers_id'), table_name='student_test_answers')
    op.drop_table('student_test_answers')
    op.drop_index(op.f('ix_student_exam_answers_id'), table_name='student_exam_answers')
    op.drop_table('student_exam_answers')
    op.drop_index(op.f('ix_lecture_links_id'), table_name='lecture_links')
    op.drop_table('lecture_links')
    op.drop_index(op.f('ix_lecture_files_id'), table_name='lecture_files')
    op.drop_table('lecture_files')
    op.drop_index(op.f('ix_exam_matching_right_id'), table_name='exam_matching_right')
    op.drop_table('exam_matching_right')
    op.drop_index(op.f('ix_exam_answers_id'), table_name='exam_answers')
    op.drop_table('exam_answers')
    op.drop_index(op.f('ix_user_notes_id'), table_name='user_notes')
    op.drop_table('user_notes')
    op.drop_index(op.f('ix_test_questions_id'), table_name='test_questions')
    op.drop_table('test_questions')
    op.drop_index(op.f('ix_student_test_attempts_id'), table_name='student_test_attempts')
    op.drop_table('student_test_attempts')
    op.drop_index(op.f('ix_student_exam_attempts_id'), table_name='student_exam_attempts')
    op.drop_table('student_exam_attempts')
    op.drop_index(op.f('ix_message_files_id'), table_name='message_files')
    op.drop_table('message_files')
    op.drop_index(op.f('ix_lecture_attributes_id'), table_name='lecture_attributes')
    op.drop_table('lecture_attributes')
    op.drop_index(op.f('ix_exam_questions_id'), table_name='exam_questions')
    op.drop_table('exam_questions')
    op.drop_index(op.f('ix_tests_id'), table_name='tests')
    op.drop_table('tests')
    op.drop_index(op.f('ix_student_lessons_id'), table_name='student_lessons')
    op.drop_table('student_lessons')
    op.drop_index(op.f('ix_lectures_id'), table_name='lectures')
    op.drop_table('lectures')
    op.drop_index(op.f('ix_exams_id'), table_name='exams')
    op.drop_table('exams')
    op.drop_index(op.f('ix_chat_messages_id'), table_name='chat_messages')
    op.drop_table('chat_messages')
    op.drop_index(op.f('ix_user_folders_id'), table_name='user_folders')
    op.drop_table('user_folders')
    op.drop_index(op.f('ix_student_course_association_student_id'), table_name='student_course_association')
    op.drop_index(op.f('ix_student_course_association_course_id'), table_name='student_course_association')
    op.drop_table('student_course_association')
    op.drop_index(op.f('ix_lessons_id'), table_name='lessons')
    op.drop_table('lessons')
    op.drop_index(op.f('ix_instruction_files_id'), table_name='instruction_files')
    op.drop_table('instruction_files')
    op.drop_index(op.f('ix_course_icons_id'), table_name='course_icons')
    op.drop_table('course_icons')
    op.drop_index(op.f('ix_course_certificates_id'), table_name='course_certificates')
    op.drop_table('course_certificates')
    op.drop_index(op.f('ix_chat_id'), table_name='chat')
    op.drop_table('chat')
    op.drop_index(op.f('ix_category_certificates_id'), table_name='category_certificates')
    op.drop_table('category_certificates')
    op.drop_index(op.f('ix_students_id'), table_name='students')
    op.drop_table('students')
    op.drop_index(op.f('ix_reset_password_links_id'), table_name='reset_password_links')
    op.drop_table('reset_password_links')
    op.drop_index(op.f('ix_moderators_id'), table_name='moderators')
    op.drop_table('moderators')
    op.drop_index(op.f('ix_instructions_id'), table_name='instructions')
    op.drop_table('instructions')
    op.drop_index(op.f('ix_images_id'), table_name='images')
    op.drop_table('images')
    op.drop_index(op.f('ix_courses_id'), table_name='courses')
    op.drop_table('courses')
    op.drop_index(op.f('ix_activate_codes_id'), table_name='activate_codes')
    op.drop_table('activate_codes')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_categories_id'), table_name='categories')
    op.drop_table('categories')
    # ### end Alembic commands ###
