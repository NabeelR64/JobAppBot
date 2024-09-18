import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';  // Required for ngModel


@Component({
  selector: 'app-search-form',
  standalone: true,  // Make it standalone
  imports: [FormsModule], 
  templateUrl: './search-form.component.html',
  styleUrls: ['./search-form.component.css']
})
export class SearchFormComponent {
  experienceLevels: string[] = ['Entry', 'Mid', 'Senior'];
  selectedExperienceLevel: string = '';
  location: string = '';

  searchJobs(): void {
    console.log('Searching jobs for:', this.selectedExperienceLevel, this.location);
    // Implement the logic to trigger search here
  }
}
