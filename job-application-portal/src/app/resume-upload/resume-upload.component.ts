import { Component } from '@angular/core';
import { ResumeService } from '../resume.service';

@Component({
  selector: 'app-resume-upload',
  standalone: true,
  templateUrl: './resume-upload.component.html',
  styleUrls: ['./resume-upload.component.css']
})
export class ResumeUploadComponent {
  fileToUpload: File | null = null;
  jobSuggestions: string[] = [];
  errorMessage: string = '';

  constructor(private resumeService: ResumeService) { }

  handleFileInput(event: any): void {
    this.fileToUpload = event.target.files[0];
  }

  uploadFile(): void {
    if (this.fileToUpload) {
      this.resumeService.uploadResume(this.fileToUpload).subscribe(
        (response) => {
          this.jobSuggestions = response.suggested_roles;
          console.log(response.suggested_roles);
        },
        (error) => {
          this.errorMessage = 'Error uploading resume';
        }
      );
    }
  }
}
