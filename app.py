// app.js - JavaScript for Gospel Grace Education System
// FIXED: Updated to your Render backend URL
const API_BASE = 'https://gospelgraceeduofficalapp-com.onrender.com/api';
let currentUser = null;
let allStudents = [];
let attendanceStudents = [];

// Set default date for attendance
window.onload = function() {
    const today = new Date().toISOString().split('T')[0];
    document.getElementById('attendanceDate').value = today;
    checkAuth();
    
    // Initialize certificate preview
    renderCertificatePreview({
        studentName: "[STUDENT NAME]",
        courseName: "[COURSE NAME]",
        duration: "3 Months",
        grade: "A (Excellent)",
        completionDate: new Date().toLocaleDateString(),
        certId: "CERT-XXXXXXXXXX",
        issueDate: new Date().toLocaleDateString()
    });
};

// Function to render certificate preview
function renderCertificatePreview(data) {
    const certificateHTML = `
        <!-- Golden Border -->
        <div style="position: absolute; top: 15mm; left: 15mm; right: 15mm; bottom: 15mm; border: 10mm solid #d4af37; padding: 20mm; background: #fffaf0; height: calc(297mm - 50mm); box-sizing: border-box;">
            
            <!-- Decorative Corner Elements -->
            <div style="position: absolute; top: -5mm; left: -5mm; width: 20mm; height: 20mm; border-top: 3mm solid #8b4513; border-left: 3mm solid #8b4513;"></div>
            <div style="position: absolute; top: -5mm; right: -5mm; width: 20mm; height: 20mm; border-top: 3mm solid #8b4513; border-right: 3mm solid #8b4513;"></div>
            <div style="position: absolute; bottom: -5mm; left: -5mm; width: 20mm; height: 20mm; border-bottom: 3mm solid #8b4513; border-left: 3mm solid #8b4513;"></div>
            <div style="position: absolute; bottom: -5mm; right: -5mm; width: 20mm; height: 20mm; border-bottom: 3mm solid #8b4513; border-right: 3mm solid #8b4513;"></div>
            
            <!-- Inner Border -->
            <div style="position: absolute; top: 5mm; left: 5mm; right: 5mm; bottom: 5mm; border: 1px solid rgba(212, 175, 55, 0.3); pointer-events: none;"></div>
            
            <!-- Certificate Content -->
            <div style="height: 100%; display: flex; flex-direction: column; justify-content: space-between; padding: 10mm;">
                
                <!-- Header Section -->
                <div style="text-align: center; margin-bottom: 20mm;">
                    <div style="margin-bottom: 10mm;">
                        <h1 style="color: #1e3c72; font-size: 36px; margin: 0; text-transform: uppercase; letter-spacing: 2px; font-weight: bold;">
                            CERTIFICATE
                        </h1>
                        <h2 style="color: #1e3c72; font-size: 24px; margin: 5px 0 0 0; font-weight: normal;">
                            OF COMPLETION
                        </h2>
                    </div>
                    
                    <div style="height: 2px; background: linear-gradient(90deg, transparent, #d4af37, transparent); margin: 10mm auto; width: 70%;"></div>
                    
                    <p style="color: #666; font-size: 16px; margin-top: 10mm; font-style: italic;">
                        This Certificate is Awarded to
                    </p>
                </div>
                
                <!-- Student Name Section -->
                <div style="text-align: center; margin: 15mm 0;">
                    <div style="display: inline-block; padding: 15mm 30mm; background: linear-gradient(to right, rgba(212, 175, 55, 0.1), rgba(255, 215, 0, 0.1)); border-radius: 8px; border: 1.5mm solid #d4af37;">
                        <h2 style="font-size: 36px; color: #8b4513; margin: 0; font-weight: bold; text-transform: uppercase; line-height: 1.2;" 
                            id="previewName">
                            ${data.studentName}
                        </h2>
                    </div>
                </div>
                
                <!-- Certificate Body -->
                <div style="text-align: center; margin: 15mm 0; flex-grow: 1;">
                    <p style="font-size: 20px; margin: 10mm 0; color: #333; line-height: 1.5;">
                        for successfully completing the course in
                    </p>
                    
                    <h3 style="font-size: 28px; color: #1e3c72; margin: 15mm 0; font-weight: bold; text-decoration: underline; text-decoration-color: #d4af37;" 
                        id="previewCourse">
                        ${data.courseName}
                    </h3>
                    
                    <div style="margin: 20mm auto; padding: 15mm; border: 1.5mm dashed #d4af37; border-radius: 6px; background: rgba(255, 255, 255, 0.8); max-width: 400px;">
                        <div style="display: flex; justify-content: space-around; flex-wrap: wrap;">
                            <div style="text-align: center; margin: 5mm 10mm;">
                                <p style="font-size: 14px; margin: 2mm 0; color: #666;"><strong>Duration:</strong></p>
                                <p style="font-size: 16px; color: #1e3c72; font-weight: bold;" id="previewDuration">${data.duration}</p>
                            </div>
                            <div style="text-align: center; margin: 5mm 10mm;">
                                <p style="font-size: 14px; margin: 2mm 0; color: #666;"><strong>Grade:</strong></p>
                                <p style="font-size: 16px; color: #d4af37; font-weight: bold;" id="previewGrade">${data.grade}</p>
                            </div>
                            <div style="text-align: center; margin: 5mm 10mm;">
                                <p style="font-size: 14px; margin: 2mm 0; color: #666;"><strong>Completed:</strong></p>
                                <p style="font-size: 16px; color: #1e3c72; font-weight: bold;" id="previewDate">${data.completionDate}</p>
                            </div>
                        </div>
                    </div>
                    
                    <p style="font-size: 18px; margin: 20mm 0 15mm 0; color: #333; font-style: italic;">
                        In recognition of dedication, hard work, and outstanding achievement
                    </p>
                    
                    <p style="font-size: 16px; color: #666; margin-top: 15mm;">
                        Issued on: <span id="previewIssueDate" style="color: #1e3c72; font-weight: bold;">${data.issueDate}</span>
                    </p>
                </div>
                
                <!-- Signatures Section -->
                <div style="display: flex; justify-content: space-between; margin-top: 20mm; padding-top: 10mm; border-top: 1.5mm solid #d4af37;">
                    
                    <!-- Founder Signature -->
                    <div style="text-align: center; flex: 1;">
                        <div style="margin-top: 10mm;">
                            <div style="height: 40mm; margin-bottom: 5mm;">
                                <!-- Signature line -->
                                <div style="width: 150mm; height: 1px; background: #333; margin: 0 auto 2mm auto;"></div>
                                <div style="width: 150mm; height: 1px; background: #333; margin: 0 auto;"></div>
                            </div>
                            <strong style="font-size: 16px; color: #1e3c72; display: block;">Mr. Amey Lole</strong>
                            <span style="color: #666; font-size: 14px;">FOUNDER & DIRECTOR</span><br>
                            <span style="color: #666; font-size: 12px;">Gospel Grace Education</span>
                        </div>
                    </div>
                    
                    <!-- Institute Seal -->
                    <div style="text-align: center; flex: 1;">
                        <div style="position: relative; height: 70mm; margin: 5mm auto 10mm auto;">
                            <div style="position: absolute; top: 0; left: 50%; transform: translateX(-50%); width: 70mm; height: 70mm; border: 2mm solid #d4af37; border-radius: 50%; display: flex; align-items: center; justify-content: center; background: white;">
                                <div style="text-align: center;">
                                    <div style="font-size: 12px; color: #666; font-weight: bold;">SEAL</div>
                                    <div style="font-size: 10px; color: #666;">GOSPEL GRACE</div>
                                </div>
                            </div>
                        </div>
                        <strong style="font-size: 16px; color: #1e3c72; display: block;">Authorized Signature</strong>
                        <span style="color: #666; font-size: 14px;">Institute Stamp</span><br>
                        <span style="color: #666; font-size: 12px;">Official Verification</span>
                    </div>
                </div>
                
                <!-- Footer -->
                <div style="text-align: center; margin-top: 15mm; color: #666; font-size: 10px; padding-top: 10mm; border-top: 1px solid #ddd;">
                    <p><strong>Certificate ID:</strong> <span id="previewCertId" style="color: #1e3c72; font-weight: bold;">${data.certId}</span></p>
                    <p style="margin-top: 2mm; color: #888;">
                        This certificate is issued electronically and can be verified at Gospel Grace Education
                    </p>
                </div>
            </div>
        </div>
    `;
    
    document.getElementById('certificatePreview').innerHTML = certificateHTML;
}

// Authentication Functions
function showLogin() {
    document.getElementById('loginModal').style.display = 'block';
}

function hideLogin() {
    document.getElementById('loginModal').style.display = 'none';
    document.getElementById('loginMessage').style.display = 'none';
}

// FIXED: Correct login function
async function login() {
    const username = document.getElementById('loginUsername').value;
    const password = document.getElementById('loginPassword').value;
    
    if (!username || !password) {
        showMessage('loginMessage', 'Please enter username and password', 'error');
        return;
    }
    
    try {
        // FIXED: Correct endpoint is /auth/login
        const response = await fetch(`${API_BASE}/auth/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password }),
            credentials: 'include' // Important for sessions
        });
        
        const result = await response.json();
        
        if(result.success) {
            currentUser = result.user;
            document.getElementById('loginSection').style.display = 'none';
            document.getElementById('userInfo').style.display = 'block';
            document.getElementById('userName').textContent = currentUser.full_name || currentUser.username;
            hideLogin();
            
            // Show UI elements
            document.getElementById('navTabs').style.display = 'flex';
            document.getElementById('mainSearchBar').style.display = 'flex';
            
            // Update UI based on role
            updateUIForRole(currentUser.role);
            
            // Load initial data
            loadDashboard();
            loadStudents();
            loadFAQ();
            
            showMessage('dashboardMessage', `Welcome ${currentUser.full_name}!`, 'success');
        } else {
            showMessage('loginMessage', `Error: ${result.message}`, 'error');
        }
    } catch (error) {
        showMessage('loginMessage', `Error: ${error.message}`, 'error');
    }
}

async function logout() {
    try {
        // FIXED: Correct endpoint is /auth/logout
        await fetch(`${API_BASE}/auth/logout`, { 
            method: 'POST',
            credentials: 'include'
        });
        currentUser = null;
        document.getElementById('loginSection').style.display = 'block';
        document.getElementById('userInfo').style.display = 'none';
        
        // Hide UI elements
        document.getElementById('navTabs').style.display = 'none';
        document.getElementById('mainSearchBar').style.display = 'none';
        
        // Clear all data displays
        document.getElementById('recentStudents').innerHTML = '<p>Please login to view students</p>';
        document.getElementById('studentList').innerHTML = '<p>Please login to view students</p>';
        document.getElementById('studentStats').innerHTML = '<p>Please login to view reports</p>';
        document.getElementById('feeStats').innerHTML = '<p>Please login to view fee reports</p>';
        document.getElementById('attendanceStats').innerHTML = '<p>Please login to view attendance</p>';
        
        // Show login modal
        showLogin();
    } catch (error) {
        console.error('Logout error:', error);
    }
}

// FIXED: Check authentication status
async function checkAuth() {
    try {
        const response = await fetch(`${API_BASE}/auth/check`, {
            credentials: 'include'
        });
        const result = await response.json();
        
        if(result.authenticated) {
            currentUser = result.user;
            document.getElementById('loginSection').style.display = 'none';
            document.getElementById('userInfo').style.display = 'block';
            document.getElementById('userName').textContent = currentUser.full_name || currentUser.username;
            
            // Show UI elements
            document.getElementById('navTabs').style.display = 'flex';
            document.getElementById('mainSearchBar').style.display = 'flex';
            
            updateUIForRole(currentUser.role);
            
            // Load initial data
            loadDashboard();
            loadStudents();
            loadFAQ();
        } else {
            // Not logged in, show login modal
            setTimeout(showLogin, 1000);
        }
    } catch (error) {
        // Not logged in, show login modal
        setTimeout(showLogin, 1000);
    }
}

function updateUIForRole(role) {
    const attendanceTab = document.getElementById('attendanceTab');
    const feesTab = document.getElementById('feesTab');
    const certificateTab = document.getElementById('certificateTab');
    const addStudentCard = document.getElementById('addStudentCard');
    const addStudentBtn = document.getElementById('addStudentBtn');
    const recordFeeBtn = document.getElementById('recordFeeBtn');
    const markAttendanceBtn = document.getElementById('markAttendanceBtn');
    const generateCertBtn = document.getElementById('generateCertBtn');
    
    if (role === 'teacher') {
        // Teacher can only see dashboard, students, attendance, and reports
        attendanceTab.classList.remove('hidden');
        feesTab.classList.add('hidden');
        certificateTab.classList.add('hidden');
        
        // Hide action buttons and forms
        addStudentCard.style.display = 'none';
        addStudentBtn.style.display = 'none';
        recordFeeBtn.style.display = 'none';
        generateCertBtn.style.display = 'none';
        markAttendanceBtn.style.display = 'block';
    } else if (role === 'admin') {
        // Admin can see everything
        attendanceTab.classList.remove('hidden');
        feesTab.classList.remove('hidden');
        certificateTab.classList.remove('hidden');
        
        // Show all action buttons
        addStudentCard.style.display = 'block';
        addStudentBtn.style.display = 'block';
        recordFeeBtn.style.display = 'block';
        generateCertBtn.style.display = 'block';
        markAttendanceBtn.style.display = 'block';
    }
    
    updateButtonStates();
}

function updateButtonStates() {
    if (!currentUser) return;
    
    const addStudentBtn = document.getElementById('addStudentBtn');
    const recordFeeBtn = document.getElementById('recordFeeBtn');
    const generateCertBtn = document.getElementById('generateCertBtn');
    
    if (currentUser.role === 'teacher') {
        addStudentBtn.disabled = true;
        recordFeeBtn.disabled = true;
        generateCertBtn.disabled = true;
        addStudentBtn.style.opacity = '0.5';
        recordFeeBtn.style.opacity = '0.5';
        generateCertBtn.style.opacity = '0.5';
    } else {
        addStudentBtn.disabled = false;
        recordFeeBtn.disabled = false;
        generateCertBtn.disabled = false;
        addStudentBtn.style.opacity = '1';
        recordFeeBtn.style.opacity = '1';
        generateCertBtn.style.opacity = '1';
    }
}

// Tab switching
function switchTab(tabName) {
    if (!currentUser) {
        showLogin();
        return;
    }
    
    // Hide all tabs
    document.querySelectorAll('.tab-content').forEach(tab => {
        tab.classList.remove('active');
    });
    
    // Show selected tab
    const tabElement = document.getElementById(tabName);
    if (tabElement) {
        tabElement.classList.add('active');
        
        // Load data for the tab
        if(tabName === 'dashboard') {
            loadDashboard();
        } else if(tabName === 'student') {
            loadStudents();
        } else if(tabName === 'attendance') {
            loadAttendanceStudents();
        } else if(tabName === 'reports') {
            loadReports();
        }
    }
    
    // Update tab navigation
    document.querySelectorAll('.tab').forEach(tab => {
        tab.classList.remove('active');
        if (tab.textContent.includes(tabName.charAt(0).toUpperCase() + tabName.slice(1))) {
            tab.classList.add('active');
        }
    });
}

// Show message
function showMessage(elementId, message, type = 'success') {
    const element = document.getElementById(elementId);
    element.textContent = message;
    element.className = `message ${type}`;
    element.style.display = 'block';
    
    setTimeout(() => {
        element.style.display = 'none';
    }, 5000);
}

// Global search functionality
async function performSearch() {
    if (!currentUser) {
        showLogin();
        return;
    }
    
    const searchTerm = document.getElementById('globalSearch').value.trim();
    if (!searchTerm) {
        alert('Please enter a search term');
        return;
    }
    
    try {
        const response = await fetch(`${API_BASE}/admin/students`);
        const result = await response.json();
        
        if (result.success) {
            const students = result.students;
            const filtered = students.filter(student => 
                student.full_name.toLowerCase().includes(searchTerm.toLowerCase()) ||
                student.email.toLowerCase().includes(searchTerm.toLowerCase()) ||
                student.phone.includes(searchTerm)
            );
            
            if (filtered.length === 0) {
                alert('No students found matching your search');
                return;
            }
            
            displayStudents(filtered);
            switchTab('student');
        }
    } catch (error) {
        console.error('Search error:', error);
        alert('Error performing search');
    }
}

function clearSearch() {
    document.getElementById('globalSearch').value = '';
    loadStudents();
}

// Student search in student tab
async function searchStudents() {
    const searchTerm = document.getElementById('studentSearch').value.trim();
    if (!searchTerm) {
        loadStudents();
        return;
    }
    
    try {
        const response = await fetch(`${API_BASE}/admin/students`);
        const result = await response.json();
        
        if (result.success) {
            const students = result.students;
            const filtered = students.filter(student => 
                student.full_name.toLowerCase().includes(searchTerm.toLowerCase()) ||
                student.email.toLowerCase().includes(searchTerm.toLowerCase()) ||
                student.phone.includes(searchTerm)
            );
            
            displayStudents(filtered);
        }
    } catch (error) {
        console.error('Search error:', error);
        showMessage('studentMessage', 'Error searching students', 'error');
    }
}

function clearStudentSearch() {
    document.getElementById('studentSearch').value = '';
    loadStudents();
}

// Load dashboard data
async function loadDashboard() {
    if (!currentUser) return;
    
    try {
        if (currentUser.role === 'admin') {
            const response = await fetch(`${API_BASE}/admin/dashboard/stats`, {
                credentials: 'include'
            });
            const result = await response.json();
            
            if (result.success) {
                // Display stats can be added here
            }
        }
        
        // Load recent students
        const response = await fetch(`${API_BASE}/admin/students`, {
            credentials: 'include'
        });
        const result = await response.json();
        
        if (result.success) {
            const recentStudents = result.students.slice(-5).reverse();
            const html = recentStudents.map(student => `
                <div class="student-item">
                    <div>
                        <strong>${student.full_name}</strong><br>
                        <small>${student.course}</small>
                    </div>
                    <div>
                        <small>${student.email}</small><br>
                        <small>${student.phone}</small>
                    </div>
                </div>
            `).join('');
            
            document.getElementById('recentStudents').innerHTML = html || '<p>No students found</p>';
        }
    } catch (error) {
        console.error('Error loading dashboard:', error);
    }
}

// Load all students
async function loadStudents() {
    if (!currentUser) return;
    
    try {
        let response;
        if (currentUser.role === 'admin') {
            response = await fetch(`${API_BASE}/admin/students`, {
                credentials: 'include'
            });
        } else if (currentUser.role === 'teacher') {
            response = await fetch(`${API_BASE}/teacher/students`, {
                credentials: 'include'
            });
        }
        
        if (response) {
            const result = await response.json();
            if (result.success) {
                allStudents = result.students;
                displayStudents(allStudents);
            }
        }
    } catch (error) {
        console.error('Error loading students:', error);
        showMessage('studentMessage', 'Error loading students', 'error');
    }
}

function displayStudents(students) {
    const html = students.map(student => `
        <div class="student-item">
            <div>
                <strong>${student.full_name}</strong><br>
                <small>${student.course}</small><br>
                <small>${student.email} | ${student.phone}</small>
            </div>
            <div class="action-buttons">
                <button onclick="viewStudentDetails('${student._id}')" class="action-btn btn">
                    View
                </button>
                ${currentUser && currentUser.role === 'admin' ? `
                <button onclick="deleteStudent('${student._id}')" class="action-btn btn-danger">
                    Delete
                </button>
                ` : ''}
            </div>
        </div>
    `).join('');
    
    document.getElementById('studentList').innerHTML = html || '<p>No students found</p>';
}

// Add new student
async function addStudent(event) {
    event.preventDefault();
    
    if (!currentUser || currentUser.role !== 'admin') {
        alert('Only admin can add students');
        return;
    }
    
    const form = event.target;
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());
    
    try {
        const response = await fetch(`${API_BASE}/admin/students/add`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            credentials: 'include',
            body: JSON.stringify(data)
        });
        
        const result = await response.json();
        
        if(result.success) {
            showMessage('studentMessage', `Student added successfully! Student ID: ${result.student_id}`, 'success');
            form.reset();
            loadStudents();
            loadDashboard();
        } else {
            showMessage('studentMessage', `Error: ${result.message}`, 'error');
        }
    } catch (error) {
        showMessage('studentMessage', `Error: ${error.message}`, 'error');
    }
}

// Delete student
async function deleteStudent(studentId) {
    if (!currentUser || currentUser.role !== 'admin') {
        alert('Only admin can delete students');
        return;
    }
    
    if (!confirm('Are you sure you want to delete this student?')) {
        return;
    }
    
    try {
        const response = await fetch(`${API_BASE}/admin/students/${studentId}`, {
            method: 'DELETE',
            credentials: 'include'
        });
        
        const result = await response.json();
        
        if(result.success) {
            showMessage('studentMessage', 'Student deleted successfully!', 'success');
            loadStudents();
            loadDashboard();
        } else {
            showMessage('studentMessage', `Error: ${result.message}`, 'error');
        }
    } catch (error) {
        showMessage('studentMessage', `Error: ${error.message}`, 'error');
    }
}

// View student details
async function viewStudentDetails(studentId) {
    try {
        let response;
        if (currentUser.role === 'admin') {
            response = await fetch(`${API_BASE}/admin/students`);
        } else {
            response = await fetch(`${API_BASE}/teacher/students`);
        }
        
        const result = await response.json();
        if (result.success) {
            const student = result.students.find(s => s._id === studentId);
            if (student) {
                alert(`Student Details:\n\nName: ${student.full_name}\nEmail: ${student.email}\nPhone: ${student.phone}\nCourse: ${student.course}\nAddress: ${student.address || 'N/A'}\nFather: ${student.father_name || 'N/A'}\nMother: ${student.mother_name || 'N/A'}`);
            }
        }
    } catch (error) {
        console.error('Error viewing student details:', error);
    }
}

// Generate certificate
async function generateCertificate(event) {
    event.preventDefault();
    
    if (!currentUser || currentUser.role !== 'admin') {
        alert('Only admin can generate certificates');
        return;
    }
    
    const form = event.target;
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());
    
    const studentName = document.getElementById('certStudentName').value;
    
    if (!studentName) {
        showMessage('certMessage', 'Please enter student name', 'error');
        return;
    }
    
    // Generate certificate ID
    const certId = `CERT-${Date.now().toString().slice(-10)}`;
    const completionDate = data.completion_date || new Date().toLocaleDateString();
    const issueDate = new Date().toLocaleDateString();
    const duration = data.duration || '3 Months';
    const grade = data.grade + ' (' + (data.grade === 'A' ? 'Excellent' : data.grade === 'B' ? 'Very Good' : 'Good') + ')';
    
    // Update preview
    renderCertificatePreview({
        studentName: studentName.toUpperCase(),
        courseName: data.course_name.toUpperCase(),
        duration: duration,
        grade: grade,
        completionDate: completionDate,
        certId: certId,
        issueDate: issueDate
    });
    
    showMessage('certMessage', `Certificate generated successfully! Certificate ID: ${certId}`, 'success');
}

// Print certificate
function printCertificate() {
    if (!currentUser || currentUser.role !== 'admin') {
        alert('Only admin can print certificates');
        return;
    }
    
    const certificateHTML = document.getElementById('certificatePreview').innerHTML;
    
    const printContent = `
        <!DOCTYPE html>
        <html>
        <head>
            <title>Certificate - Gospel Grace Education</title>
            <style>
                @page {
                    size: A4;
                    margin: 0;
                }
                body {
                    margin: 0;
                    padding: 0;
                    width: 210mm;
                    height: 297mm;
                    overflow: hidden;
                    font-family: 'Times New Roman', serif;
                }
                .certificate-container {
                    width: 210mm;
                    height: 297mm;
                    position: relative;
                    background: white;
                }
                * {
                    box-sizing: border-box;
                }
            </style>
        </head>
        <body>
            <div class="certificate-container">
                ${certificateHTML}
            </div>
            <script>
                window.onload = function() {
                    window.print();
                    setTimeout(function() {
                        window.close();
                    }, 500);
                };
            <\/script>
        </body>
        </html>
    `;
    
    const printWindow = window.open('', '_blank');
    printWindow.document.write(printContent);
    printWindow.document.close();
}

// Load FAQ
async function loadFAQ() {
    try {
        const defaultFAQ = [
            {
                question: 'How do I add a new student?',
                answer: 'Go to Students tab, fill in all required fields including course fees and initial payment, then click Register Student.'
            },
            {
                question: 'How can I search for a student?',
                answer: 'Use the search bar at the top of the page or the search box in the Students tab. You can search by Student ID, Name, Phone, or Email.'
            }
        ];
        document.getElementById('faqList').innerHTML = defaultFAQ.map((item, index) => `
            <div class="faq-item">
                <div class="faq-question" onclick="toggleFAQ(${index})">
                    <span>${item.question}</span>
                    <span>▼</span>
                </div>
                <div class="faq-answer" id="faqAnswer${index}">
                    ${item.answer}
                </div>
            </div>
        `).join('');
    } catch (error) {
        console.error('Error loading FAQ:', error);
    }
}

function toggleFAQ(index) {
    const answer = document.getElementById(`faqAnswer${index}`);
    answer.classList.toggle('active');
}

// Load reports
async function loadReports() {
    if (!currentUser) return;
    
    try {
        let response;
        if (currentUser.role === 'admin') {
            response = await fetch(`${API_BASE}/admin/dashboard/stats`, {
                credentials: 'include'
            });
        } else if (currentUser.role === 'teacher') {
            response = await fetch(`${API_BASE}/teacher/dashboard/stats`, {
                credentials: 'include'
            });
        }
        
        if (response) {
            const result = await response.json();
            if (result.success) {
                // Display stats
                let statsHtml = '';
                if (currentUser.role === 'admin') {
                    statsHtml = `
                        <p><strong>Total Students:</strong> ${result.stats?.students || 0}</p>
                        <p><strong>Total Teachers:</strong> ${result.stats?.teachers || 0}</p>
                        <p><strong>Total Courses:</strong> ${result.stats?.courses || 0}</p>
                    `;
                } else {
                    statsHtml = `
                        <p><strong>Assigned Students:</strong> ${result.stats?.assigned_students || 0}</p>
                        <p><strong>Pending Tasks:</strong> ${result.stats?.pending_tasks || 0}</p>
                        <p><strong>Completed Sessions:</strong> ${result.stats?.completed_sessions || 0}</p>
                    `;
                }
                document.getElementById('studentStats').innerHTML = statsHtml;
            }
        }
    } catch (error) {
        console.error('Error loading reports:', error);
    }
}

// Attendance functions
async function loadAttendanceStudents() {
    if (!currentUser) return;
    
    try {
        let response;
        if (currentUser.role === 'admin') {
            response = await fetch(`${API_BASE}/admin/students`, {
                credentials: 'include'
            });
        } else if (currentUser.role === 'teacher') {
            response = await fetch(`${API_BASE}/teacher/students`, {
                credentials: 'include'
            });
        }
        
        if (response) {
            const result = await response.json();
            if (result.success) {
                attendanceStudents = result.students;
                renderAttendanceGrid();
            }
        }
    } catch (error) {
        console.error('Error loading attendance students:', error);
    }
}

function renderAttendanceGrid(filter = '') {
    const filteredStudents = attendanceStudents.filter(student => 
        student.full_name.toLowerCase().includes(filter.toLowerCase()) ||
        student.course.toLowerCase().includes(filter.toLowerCase())
    );
    
    const html = filteredStudents.map(student => `
        <div class="attendance-item" data-student-id="${student._id}" onclick="toggleAttendance(this, '${student._id}')">
            <strong>${student.full_name}</strong><br>
            <small>${student.course}</small><br>
        </div>
    `).join('');
    
    document.getElementById('attendanceGrid').innerHTML = html || '<p>No students found</p>';
}

function filterAttendanceStudents() {
    const filter = document.getElementById('attendanceSearch').value;
    renderAttendanceGrid(filter);
}

function toggleAttendance(element, studentId) {
    if (!currentUser) return;
    
    // Toggle between present and absent
    if (element.classList.contains('present')) {
        element.classList.remove('present');
        element.classList.add('absent');
        element.innerHTML += `<br><small class="status-absent">Absent</small>`;
    } else if (element.classList.contains('absent')) {
        element.classList.remove('absent');
        element.querySelector('small.status-absent')?.remove();
    } else {
        element.classList.add('present');
        element.innerHTML += `<br><small class="status-present">Present</small>`;
    }
}

async function saveAttendance() {
    if (!currentUser) return;
    
    const date = document.getElementById('attendanceDate').value;
    if (!date) {
        showMessage('attendanceMessage', 'Please select a date', 'error');
        return;
    }
    
    const attendanceItems = document.querySelectorAll('.attendance-item.present, .attendance-item.absent');
    if (attendanceItems.length === 0) {
        showMessage('attendanceMessage', 'No attendance marked', 'error');
        return;
    }
    
    showMessage('attendanceMessage', 'Attendance feature coming soon!', 'info');
}
