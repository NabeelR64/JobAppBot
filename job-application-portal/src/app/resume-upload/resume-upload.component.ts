import { Component } from '@angular/core';
import { CommonModule } from '@angular/common'; // Import CommonModule
import { ResumeService } from '../resume.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-resume-upload',
  standalone: true,
  imports: [CommonModule], // Add CommonModule here
  templateUrl: './resume-upload.component.html',
  styleUrls: ['./resume-upload.component.css'],
  imports: [CommonModule]
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
          console.log("raaaaaaaa" + response.suggested_roles);
        },
        (error) => {
          this.errorMessage = 'Error uploading resume';
        }
      );
    }
  }
}