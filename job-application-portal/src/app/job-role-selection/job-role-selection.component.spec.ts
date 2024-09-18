import { ComponentFixture, TestBed } from '@angular/core/testing';

import { JobRoleSelectionComponent } from './job-role-selection.component';

describe('JobRoleSelectionComponent', () => {
  let component: JobRoleSelectionComponent;
  let fixture: ComponentFixture<JobRoleSelectionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [JobRoleSelectionComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(JobRoleSelectionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
