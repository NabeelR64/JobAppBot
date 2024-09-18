import { NgFor, NgIf } from '@angular/common';
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-job-role-selection',
  standalone: true,
  imports: [NgIf, NgFor],
  templateUrl: './job-role-selection.component.html',
  styleUrl: './job-role-selection.component.css'
})
export class JobRoleSelectionComponent {
  @Input() jobSuggestions: string[] = [];

}


