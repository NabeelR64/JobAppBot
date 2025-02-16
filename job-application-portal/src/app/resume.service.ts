import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ResumeService {
  private apiUrl = 'http://127.0.0.1:1992/upload_resume';  // Adjust based on your backend

  constructor(private http: HttpClient) { }
  
  uploadResume(file: File): Observable<any> {
    const formData: FormData = new FormData();
    formData.append('file', file, file.name);
    const headers = new HttpHeaders({
      'Content-Type':'application/json',
    })
    return this.http.post<any>(this.apiUrl, formData, 
      { headers }
    );
  }
}
