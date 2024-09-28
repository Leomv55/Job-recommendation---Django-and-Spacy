import json
import os

from django.core.management.base import BaseCommand

from recommendation.models import Skill, JobPost

class Command(BaseCommand):
    help = "Create job posts as sample"

    def handle(self, *args, **kwargs):
        sample_file_path = os.path.dirname(os.path.abspath(__file__)) + "/samples/job_posts.json"
        sample_file = open(sample_file_path, "r")
        sample_content = json.load(sample_file)

        for sample_set in sample_content:
            for job_post in sample_set:
                skills = job_post.get("skills", [])
                existing_skills_details = Skill.objects.filter(name__in=skills).values_list("id", "name")
                
                existing_skill_ids = [skill_id for skill_id, _ in existing_skills_details]
                existing_skill_names = [skill_name for _, skill_name in existing_skills_details]
                remaining_skills = set(skills) - set(existing_skill_names)
                
                if remaining_skills:
                    new_skill_objects = [
                        Skill(name=remaining_skill)
                        for remaining_skill in remaining_skills
                    ]

                    remaining_skills_objects = Skill.objects.bulk_create(new_skill_objects)
                    remaining_skill_ids = [remaining_skill.id for remaining_skill in remaining_skills_objects]
                    existing_skill_ids = existing_skill_ids + remaining_skill_ids

                job_post_object = JobPost(
                    title=job_post.get("title", ""),
                    description=job_post.get("description", "")
                )
                job_post_object.save()

                job_post_object.skills.set(existing_skill_ids)
                job_post_object.save()

                print("Job Post created")
                print(f"Job Id: {job_post_object.id}")
                print(f"Job title: {job_post_object.title}")
                print(f"Job skills {job_post_object.skills}")
    