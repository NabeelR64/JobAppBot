import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { ResumeUploadComponent } from './resume-upload/resume-upload.component'; // Add this
import { JobRoleSelectionComponent } from './job-role-selection/job-role-selection.component'; // Add this
import { SearchFormComponent } from './search-form/search-form.component'; // Add this

@NgModule({
  declarations: [
    AppComponent,
    ResumeUploadComponent, // Add this
    JobRoleSelectionComponent, // Add this
    SearchFormComponent // Add this
  ],
  imports: [
    BrowserModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
