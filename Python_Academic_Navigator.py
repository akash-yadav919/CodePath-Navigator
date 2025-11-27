import json
import os
from datetime import datetime
from typing import List, Dict

class AcademicNavigator:
    def __init__(self):
        self.resources_file = 'resources.json'
        self.assessments_file = 'assessments.json'
        self.resources = self.load_data(self.resources_file)
        self.assessments = self.load_data(self.assessments_file)
        
        self.subjects = [
            'Python Basics',
            'Data Structures',
            'Object-Oriented Programming',
            'File Handling',
            'Libraries & Frameworks',
            'Web Development',
            'Data Analysis'
        ]
        
        self.resource_types = [
            'PDF', 'Document', 'Link', 'Video',
            'Jupyter Notebook', 'Python Script', 'Notes', 'Tutorial'
        ]
        
        self.assessment_types = [
            'Quiz', 'Assignment', 'Midterm', 'Final',
            'Practice Test', 'Self-Test'
        ]

    def load_data(self, filename: str) -> List[Dict]:
        """Load data from JSON file"""
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                return json.load(f)
        return []

    def save_data(self, data: List[Dict], filename: str):
        """Save data to JSON file"""
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    def clear_screen(self):
        """Clear the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_header(self, title: str):
        """Print a formatted header"""
        print("\n" + "="*60)
        print(f"  {title}")
        print("="*60 + "\n")

    def print_menu(self, options: List[str]):
        """Print menu options"""
        for i, option in enumerate(options, 1):
            print(f"  {i}. {option}")
        print()

    # ==================== RESOURCE MANAGEMENT ====================
    
    def add_resource(self):
        """Add a new study resource"""
        self.clear_screen()
        self.print_header("ADD NEW RESOURCE")
        
        title = input("Enter resource title: ").strip()
        if not title:
            print("❌ Title cannot be empty!")
            input("\nPress Enter to continue...")
            return
        
        print("\nResource Types:")
        for i, rt in enumerate(self.resource_types, 1):
            print(f"  {i}. {rt}")
        type_choice = int(input("\nSelect type (number): "))
        resource_type = self.resource_types[type_choice - 1]
        
        print("\nSubjects:")
        for i, subj in enumerate(self.subjects, 1):
            print(f"  {i}. {subj}")
        subj_choice = int(input("\nSelect subject (number): "))
        subject = self.subjects[subj_choice - 1]
        
        topic = input("Enter topic (optional): ").strip()
        url = input("Enter URL/link (optional): ").strip()
        tags_input = input("Enter tags (comma-separated, optional): ").strip()
        tags = [tag.strip() for tag in tags_input.split(',')] if tags_input else []
        
        resource = {
            'id': len(self.resources) + 1,
            'title': title,
            'type': resource_type,
            'subject': subject,
            'topic': topic,
            'url': url,
            'tags': tags,
            'date_added': datetime.now().strftime('%Y-%m-%d')
        }
        
        self.resources.append(resource)
        self.save_data(self.resources, self.resources_file)
        print(f"\n✅ Resource '{title}' added successfully!")
        input("\nPress Enter to continue...")

    def view_resources(self):
        """View all resources"""
        self.clear_screen()
        self.print_header(f"YOUR RESOURCES ({len(self.resources)} total)")
        
        if not self.resources:
            print("📚 No resources found. Add your first resource!")
            input("\nPress Enter to continue...")
            return
        
        for resource in self.resources:
            print(f"\n📄 {resource['title']}")
            print(f"   Type: {resource['type']} | Subject: {resource['subject']}")
            if resource['topic']:
                print(f"   Topic: {resource['topic']}")
            if resource['url']:
                print(f"   URL: {resource['url']}")
            if resource['tags']:
                print(f"   Tags: {', '.join(['#' + tag for tag in resource['tags']])}")
            print(f"   Added: {resource['date_added']}")
            print("-" * 60)
        
        input("\nPress Enter to continue...")

    def search_resources(self):
        """Search resources by keyword"""
        self.clear_screen()
        self.print_header("SEARCH RESOURCES")
        
        query = input("Enter search keyword: ").strip().lower()
        
        results = [r for r in self.resources if 
                   query in r['title'].lower() or
                   query in r['subject'].lower() or
                   query in r['topic'].lower() or
                   any(query in tag.lower() for tag in r['tags'])]
        
        if not results:
            print(f"\n❌ No resources found matching '{query}'")
        else:
            print(f"\n✅ Found {len(results)} resource(s):\n")
            for resource in results:
                print(f"📄 {resource['title']} ({resource['subject']})")
                if resource['topic']:
                    print(f"   Topic: {resource['topic']}")
                print("-" * 60)
        
        input("\nPress Enter to continue...")

    def delete_resource(self):
        """Delete a resource"""
        self.clear_screen()
        self.print_header("DELETE RESOURCE")
        
        if not self.resources:
            print("❌ No resources to delete!")
            input("\nPress Enter to continue...")
            return
        
        for i, resource in enumerate(self.resources, 1):
            print(f"{i}. {resource['title']} ({resource['subject']})")
        
        try:
            choice = int(input("\nEnter resource number to delete (0 to cancel): "))
            if choice == 0:
                return
            if 1 <= choice <= len(self.resources):
                deleted = self.resources.pop(choice - 1)
                self.save_data(self.resources, self.resources_file)
                print(f"\n✅ Deleted: {deleted['title']}")
            else:
                print("❌ Invalid choice!")
        except ValueError:
            print("❌ Please enter a valid number!")
        
        input("\nPress Enter to continue...")

    # ==================== PERFORMANCE TRACKING ====================
    
    def log_assessment(self):
        """Log a new assessment"""
        self.clear_screen()
        self.print_header("LOG ASSESSMENT")
        
        title = input("Enter assessment title: ").strip()
        if not title:
            print("❌ Title cannot be empty!")
            input("\nPress Enter to continue...")
            return
        
        print("\nAssessment Types:")
        for i, at in enumerate(self.assessment_types, 1):
            print(f"  {i}. {at}")
        type_choice = int(input("\nSelect type (number): "))
        assessment_type = self.assessment_types[type_choice - 1]
        
        print("\nSubjects:")
        for i, subj in enumerate(self.subjects, 1):
            print(f"  {i}. {subj}")
        subj_choice = int(input("\nSelect subject (number): "))
        subject = self.subjects[subj_choice - 1]
        
        topic = input("Enter topic (optional): ").strip()
        
        try:
            score = float(input("Enter score obtained: "))
            max_score = float(input("Enter maximum score: "))
            percentage = (score / max_score) * 100
        except ValueError:
            print("❌ Invalid score input!")
            input("\nPress Enter to continue...")
            return
        
        date = input("Enter date (YYYY-MM-DD, press Enter for today): ").strip()
        if not date:
            date = datetime.now().strftime('%Y-%m-%d')
        
        assessment = {
            'id': len(self.assessments) + 1,
            'title': title,
            'type': assessment_type,
            'subject': subject,
            'topic': topic,
            'score': score,
            'max_score': max_score,
            'percentage': round(percentage, 1),
            'date': date
        }
        
        self.assessments.append(assessment)
        self.save_data(self.assessments, self.assessments_file)
        print(f"\n✅ Assessment '{title}' logged successfully! Score: {percentage:.1f}%")
        input("\nPress Enter to continue...")

    def view_assessments(self):
        """View all assessments"""
        self.clear_screen()
        self.print_header(f"ASSESSMENT HISTORY ({len(self.assessments)} total)")
        
        if not self.assessments:
            print("📊 No assessments logged yet. Start tracking your performance!")
            input("\nPress Enter to continue...")
            return
        
        # Sort by date (most recent first)
        sorted_assessments = sorted(self.assessments, key=lambda x: x['date'], reverse=True)
        
        for assessment in sorted_assessments:
            percentage = assessment['percentage']
            if percentage >= 90:
                grade = "🟢 Excellent"
            elif percentage >= 70:
                grade = "🟡 Good"
            else:
                grade = "🔴 Needs Improvement"
            
            print(f"\n{assessment['title']} - {grade}")
            print(f"   Type: {assessment['type']} | Subject: {assessment['subject']}")
            if assessment['topic']:
                print(f"   Topic: {assessment['topic']}")
            print(f"   Score: {assessment['score']}/{assessment['max_score']} ({percentage}%)")
            print(f"   Date: {assessment['date']}")
            print("-" * 60)
        
        input("\nPress Enter to continue...")

    def delete_assessment(self):
        """Delete an assessment"""
        self.clear_screen()
        self.print_header("DELETE ASSESSMENT")
        
        if not self.assessments:
            print("❌ No assessments to delete!")
            input("\nPress Enter to continue...")
            return
        
        for i, assessment in enumerate(self.assessments, 1):
            print(f"{i}. {assessment['title']} - {assessment['percentage']}% ({assessment['date']})")
        
        try:
            choice = int(input("\nEnter assessment number to delete (0 to cancel): "))
            if choice == 0:
                return
            if 1 <= choice <= len(self.assessments):
                deleted = self.assessments.pop(choice - 1)
                self.save_data(self.assessments, self.assessments_file)
                print(f"\n✅ Deleted: {deleted['title']}")
            else:
                print("❌ Invalid choice!")
        except ValueError:
            print("❌ Please enter a valid number!")
        
        input("\nPress Enter to continue...")

    # ==================== ANALYTICS & REPORTING ====================
    
    def show_dashboard(self):
        """Display analytics dashboard"""
        self.clear_screen()
        self.print_header("📊 PERFORMANCE DASHBOARD")
        
        # Overall stats
        total_resources = len(self.resources)
        total_assessments = len(self.assessments)
        
        print(f"📚 Total Resources: {total_resources}")
        print(f"📝 Total Assessments: {total_assessments}")
        
        if not self.assessments:
            print("\n⚠️  No assessment data available yet.")
            input("\nPress Enter to continue...")
            return
        
        # Calculate overall average
        total_percentage = sum(a['percentage'] for a in self.assessments)
        overall_avg = total_percentage / len(self.assessments)
        print(f"🎯 Overall Average: {overall_avg:.1f}%")
        
        print("\n" + "="*60)
        print("SUBJECT-WISE PERFORMANCE")
        print("="*60)
        
        # Subject-wise stats
        subject_stats = {}
        for subject in self.subjects:
            subject_assessments = [a for a in self.assessments if a['subject'] == subject]
            if subject_assessments:
                avg = sum(a['percentage'] for a in subject_assessments) / len(subject_assessments)
                subject_stats[subject] = {
                    'average': avg,
                    'count': len(subject_assessments)
                }
        
        if subject_stats:
            for subject, stats in sorted(subject_stats.items(), key=lambda x: x[1]['average'], reverse=True):
                bar_length = int(stats['average'] / 5)
                bar = '█' * bar_length
                print(f"\n{subject}")
                print(f"  {bar} {stats['average']:.1f}%")
                print(f"  ({stats['count']} assessment{'s' if stats['count'] > 1 else ''})")
        
        # Topic weaknesses
        print("\n" + "="*60)
        print("⚠️  AREAS NEEDING ATTENTION (Topics < 70%)")
        print("="*60)
        
        topic_scores = {}
        for assessment in self.assessments:
            if assessment['topic']:
                topic = assessment['topic']
                if topic not in topic_scores:
                    topic_scores[topic] = {
                        'scores': [],
                        'subject': assessment['subject']
                    }
                topic_scores[topic]['scores'].append(assessment['percentage'])
        
        weaknesses = []
        for topic, data in topic_scores.items():
            avg = sum(data['scores']) / len(data['scores'])
            if avg < 70:
                weaknesses.append({
                    'topic': topic,
                    'subject': data['subject'],
                    'average': avg
                })
        
        weaknesses.sort(key=lambda x: x['average'])
        
        if weaknesses:
            for w in weaknesses[:5]:
                print(f"\n🔴 {w['topic']}")
                print(f"   Subject: {w['subject']}")
                print(f"   Average: {w['average']:.1f}%")
        else:
            print("\n✅ Great job! No weak areas identified.")
        
        input("\n\nPress Enter to continue...")

    # ==================== MAIN MENU ====================
    
    def resource_menu(self):
        """Resource management submenu"""
        while True:
            self.clear_screen()
            self.print_header("📚 RESOURCE MANAGEMENT")
            options = [
                "Add New Resource",
                "View All Resources",
                "Search Resources",
                "Delete Resource",
                "Back to Main Menu"
            ]
            self.print_menu(options)
            
            choice = input("Enter your choice: ").strip()
            
            if choice == '1':
                self.add_resource()
            elif choice == '2':
                self.view_resources()
            elif choice == '3':
                self.search_resources()
            elif choice == '4':
                self.delete_resource()
            elif choice == '5':
                break
            else:
                print("❌ Invalid choice! Please try again.")
                input("\nPress Enter to continue...")

    def performance_menu(self):
        """Performance tracking submenu"""
        while True:
            self.clear_screen()
            self.print_header("📈 PERFORMANCE TRACKING")
            options = [
                "Log New Assessment",
                "View All Assessments",
                "Delete Assessment",
                "Back to Main Menu"
            ]
            self.print_menu(options)
            
            choice = input("Enter your choice: ").strip()
            
            if choice == '1':
                self.log_assessment()
            elif choice == '2':
                self.view_assessments()
            elif choice == '3':
                self.delete_assessment()
            elif choice == '4':
                break
            else:
                print("❌ Invalid choice! Please try again.")
                input("\nPress Enter to continue...")

    def run(self):
        """Main application loop"""
        while True:
            self.clear_screen()
            self.print_header("🐍 PYTHON LEARNING NAVIGATOR")
            
            options = [
                "📊 Dashboard (Analytics)",
                "📚 Resource Management",
                "📈 Performance Tracking",
                "❌ Exit"
            ]
            self.print_menu(options)
            
            choice = input("Enter your choice: ").strip()
            
            if choice == '1':
                self.show_dashboard()
            elif choice == '2':
                self.resource_menu()
            elif choice == '3':
                self.performance_menu()
            elif choice == '4':
                print("\n👋 Thank you for using Python Learning Navigator!")
                print("Keep learning and coding! 🚀\n")
                break
            else:
                print("❌ Invalid choice! Please try again.")
                input("\nPress Enter to continue...")


# ==================== RUN APPLICATION ====================

if __name__ == "__main__":
    app = AcademicNavigator()
    app.run()