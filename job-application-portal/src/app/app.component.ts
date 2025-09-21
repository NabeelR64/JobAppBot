import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { SearchFormComponent } from './search-form/search-form.component';
import { ResumeUploadComponent } from './resume-upload/resume-upload.component';
import { JobRoleSelectionComponent } from './job-role-selection/job-role-selection.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    RouterOutlet,
    SearchFormComponent,
    ResumeUploadComponent,
    JobRoleSelectionComponent
  ],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']   // ✅ plural
})
export class AppComponent {
  title = 'job-application-portal';
  jobSuggestions: string[] = [];       // ✅ fine for now
  year: number = new Date().getFullYear(); // Add this line to define the year property
}
