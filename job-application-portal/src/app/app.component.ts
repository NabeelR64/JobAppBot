import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { SearchFormComponent } from './search-form/search-form.component';
import { ResumeUploadComponent } from './resume-upload/resume-upload.component';
import { JobRoleSelectionComponent } from './job-role-selection/job-role-selection.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, SearchFormComponent, ResumeUploadComponent, JobRoleSelectionComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'job-application-portal';
  jobSuggestions: string[] = [];
}
